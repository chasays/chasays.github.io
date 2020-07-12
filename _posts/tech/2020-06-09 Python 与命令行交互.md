

Python `subprocess` 模块是一个功能强大的库，用于启动和与子流程交互。 它附带了一些高级 api，比如调用、检查输出和运行，这些都集中在的程序运行和等待完成的子进程上。
可以用 `run` 来完成调用子进程的方式，但是对于 底层的进程创建与管理， `Popen`提供了很大的灵活性，以及处理未被常见函数覆盖的场景。
>最新源代码： https://github.com/python/cpython/tree/3.8/Lib/subprocess.py

下面谈论不直接涉及一个长时间运行的子进程。 考虑测试一些服务器——例如 HTTP、ping 服务器。 将它作为一个子进程启动，然后将客户机连接到它，并运行一些测试序列。 当完成后，希望以一种有序的方式关闭子程序。 这对于同步运行子进程的 `api` 来说是很难实现的，因此必须查看一些底层级别的 api。

最近做的项目安卓 shell 里面有些就需要这个。需要用 `adb shell xxx` 和安卓设备交互。


虽然可以使用 `subprocess.run `在一个线程中启动一个子进程，并在另一个线程中与其交互。 但是，当完成了子进程之后，要完全终止它将变得非常棘手。 如果子进程有一个有序的终止序列，那么这是可行的。 但是大多数服务器不这样做，只会等到他自己结束，或者手动结束。

## 获得所有输出时完成



第一个最简单的用例是启动一个 HTTP 服务器，与它交互，干净利落地终止它，并在完成后获取所有服务器的 stdout 和 stderr。  ，用 Python 3.7进行了测试:
```python
import subprocess
import time
def main():
    proc = subprocess.Popen(['ping', '-c', '3', '127.0.0.1'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

    try:
        time.sleep(1)
    finally:
        proc.terminate()
        try:
            outs, _ = proc.communicate(timeout=0.2)
            print('== subprocess exited with rc =', proc.returncode)
            print(outs.decode('utf-8'))
        except subprocess.TimeoutExpired:
            print('subprocess did not terminate in time')
if __name__ == '__main__':
    main()

```

子进程是一个 `HTTP` 服务器，使用 `Python` 自己的` HTTP.server` 模块，从启动它的目录中提供内容。 使用底层的 `Popen API` 异步启动进程(意味着 `Popen` 立即返回，子进程在后台运行)。


请注意在调用时传递给 Python 的 -u: 这对于避免标准输出缓冲并在进程被终止时尽可能多地查看标准输出非常关键。 在与子进程交互时，缓冲是一个严重的问题，稍后将看到更多这方面的示例。


样品的肉发生在最后一块。 `terminate`()向子进程发送一个 `SIGTERM` 信号。 然后，`proc.communicate `等待子进程退出并捕获所有的标准输出。 Communicate 有一个非常方便的超时参数，让知道子进程是否由于某种原因没有退出。 一个更复杂的技术是，如果子程序由于 `SIGTERM` 而没有退出，那么可以给子程序发送一个 `SIGKILL` (带有 `proc.kill`)。


如果你运行这个脚本，你会看到输出:
```shell
== subprocess exited with rc = -15
PING 127.0.0.1 (127.0.0.1): 56 data bytes
64 bytes from 127.0.0.1: icmp_seq=0 ttl=64 time=0.049 ms
```
子进程的返回码是 -15(负的意思是以信号结束，仅 POSIX，15是 `SIGTERM` 的数字代码)。 标准输出被正确地捕获并打印出来。

如果其中修改为暂停3s， `time.sleep(3) `，那么返回的结果就是 0.

## 启动，交互，实时输出，终止

一个相关的用例是以“实时”方式获取子进程的标准输出，而不是在最后将所有内容放在一起。 在这里，必须非常小心缓冲，因为它很容易导致程序崩溃和死锁。 Linux 进程通常在交互模式下进行行缓冲，否则进行全缓冲。 很少有进程是完全不缓冲的。 因此，在看来，不建议在小于一行的块中读取 stdout。 真的，千万别这么做。 标准 `i/o` 意味着可以按行使用(想想所有的 Unix 命令行工具是如何工作的) ; 如果需要子行粒度，stdout 不是正确的方法(使用套接字或其他方法)。


举个例子:
```python
import queue
import subprocess
import time
import threading
import urllib.request

def output_reader(proc, outq):
    for line in iter(proc.stdout.readline, b''):
        outq.put(line.decode('utf-8'))


def main():
    # Note the -u here: essential for not buffering the stdout of the subprocess
    proc = subprocess.Popen(['ping', '-c', '3', '127.0.0.1'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

    outq = queue.Queue()
    t = threading.Thread(target=output_reader, args=(proc, outq))
    t.start()

    try:
        for i in range(10):
            try:
                line = outq.get(block=False)
                print('{0}'.format(line), end='')
            except queue.Empty:
                print('got nothing')

            time.sleep(0.3)
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=0.2)
            print('== subprocess exited with rc =', proc.returncode)
        except subprocess.TimeoutExpired:
            print('subprocess did not terminate in time')

    t.join()


if __name__ == '__main__':
    main()
```


这个示例与之类似，除了标准输出的处理方式; 不再需要通信调用; 相反，`proc.wait` 只是等待子级退出(在发送 `SIGTERM` 之后)。 线程会轮询子标准输出属性，只要有新行可用，就会循环并立即打印它们。 如果运行这个示例，您将注意到子进程的 `stdout` 是实时报告的，而不是在最后报告一个错误。


 `(proc.stdout. readline，b”)`代码片段继续调用 `proc.stdout.readline()` ，直到这个调用返回一个空的字节串。 只有当关闭 `proc.stdout` 时才会发生这种情况，这种情况发生在子节点退出时。 因此，尽管看起来读线程可能永远不会终止——但它总会终止！ 只要子进程在运行，线程就会忠实地阻塞该 readline; 只要子进程终止，readline 调用返回 b” ，线程就会退出。


如果不想仅仅打印捕获的 stdout，而是要对其进行处理(比如寻找预期的模式) ，那么可以使用 Python 的线程安全队列进行组织。 读者的思路是:

```shell
PING 127.0.0.1 (127.0.0.1): 56 data bytes
64 bytes from 127.0.0.1: icmp_seq=0 ttl=64 time=0.052 ms
got nothing
got nothing
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.075 ms
got nothing
got nothing
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.115 ms

--- 127.0.0.1 ping statistics ---
== subprocess exited with rc = 0
```

## 向子进程输入数据

子流程模块文档警告不要执行这里描述的事情，因为可能会出现死锁，但有时候根本就没有选择！ 有些程序喜欢使用它们的标准输入和标准输出进行交互。 或者，您可能有一个具有交互(解释器)模式的程序，您希望对它进行测试——类似于` Python interepreter` 本身。 有时候可以一次提供这个程序的所有输入，然后检查它的输出; 这可以，也应该通过 `communicate` 来完成——这是完美的 API。 它正确地输入 stdin，完成后关闭它(这意味着许多交互式程序游戏结束) 等等。 但是，如果真的希望基于子进程以前的一些输出提供额外的输入，该怎么办呢。 下面是:
```python
def main():
    proc = subprocess.Popen(['python', '-i'],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    # To avoid deadlocks: careful to: add \n to output, flush output, use
    # readline() rather than read()
    proc.stdin.write(b'2<<3\n') ## 当将输入发送到行解释器时，不要忘记发送实际的换行符
    proc.stdin.flush() ## 将数据放入流后，始终刷新流，因为它可能会被缓冲
    print(proc.stdout.readline()) ## 从行解释器获取输入

    proc.stdin.write(b'len("chachadi")\n')
    proc.stdin.flush()
    print(proc.stdout.readline())

    proc.stdin.close()
    proc.terminate()
    proc.wait(timeout=0.2)
main()
```

结果
```shell

b'16\n'
b'8\n'
-15
```
将数据发送到子标准输入，但由于某些原因(缺少换行、缓冲等) ，它无法获得完整的输入
 然后调用 `readline` 等待回复，因为子进程仍然在等待输入完成(步骤1) ，所以的步骤2可能会永远挂起。 这是典型的僵局。


在交互的最后，关闭子进程的 `stdin` (这是可选的，但对于某些类型的子进程很有用) ，调用 `terminate`，然后等待。 最好是向子进程发送某种类型的“ `exit`”命令(对于 Python 解释器而言是 quit()) ; 这里的 `terminate` 是为了演示在其他选项不可用时必须做什么。 注意，也可以在这里使用` communicate`，而不是等待来捕获 stderr 输出。

## 使用非阻塞读线程和可阻塞线程进行交互

最后的示例演示了一个稍微更高级的场景。 假设正在测试一个长期存在的套接字服务器，并且有兴趣编排与它的复杂交互，可能是与多个并发客户机进行交互。 还希望彻底关闭线程和子进程的整个设置。 完整的代码示例在下里;  关键的部分是这个插座读取功能，意味着在它自己的线程中运行:
>https://github.com/python/cpython/blob/master/Lib/socketserver.py#215

下面的实例来自：https://stackoverflow.com/questions/268629/how-to-stop-basehttpserver-serve-forever-in-a-basehttprequesthandler-subclass

```python
import http.server

class StoppableHTTPServer(http.server.HTTPServer):
    def run(self):
        try:
            self.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            # Clean-up server (close socket, etc.)
            self.server_close()
server = StoppableHTTPServer(("127.0.0.1", 8080),
                             http.server.BaseHTTPRequestHandler)
server.run()
```

在浏览器访问 `http://localhost:8080/`， 结果如下
```shell
127.0.0.1 - - [10/Jun/2020 23:06:50] code 501, message Unsupported method ('GET')
127.0.0.1 - - [10/Jun/2020 23:06:50] "GET / HTTP/1.1" 501 -
127.0.0.1 - - [10/Jun/2020 23:06:52] code 501, message Unsupported method ('GET')
127.0.0.1 - - [10/Jun/2020 23:06:52] "GET /favicon.ico HTTP/1.1" 501 -
```


对于本文中描述的任务，没有一个万能的解决方案; 展示了一系列处理更常见情况的处理方法, Enjoy coding.
