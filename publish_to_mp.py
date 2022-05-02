import time
import urllib
import os
import json
import hashlib
import pickle
from urllib.error import URLError
import urllib.request
import requests
import markdown
from datetime import datetime
from datetime import timedelta
from pyquery import PyQuery
from pathlib import Path
from werobot import WeRoBot


CACHE = {}
# TFUG-CD
WECHAT_APP_ID = 'wx193da9cd52d2b703'
WECHAT_APP_SECRET = '479a4ffce6bcce71119fe1d57936f200'

# chasays
# WECHAT_APP_ID = 'wx90a82fb7b8e6861f'
# WECHAT_APP_SECRET = 'edbabaf47f8425102033bcc82e43c4bf'

CACHE_STORE = "cache.bin"


def dump_cache():
    with open(CACHE_STORE, "wb") as fp:
        pickle.dump(CACHE, fp)


def init_cache():
    global CACHE
    if os.path.exists(CACHE_STORE):
        with open(CACHE_STORE, "rb") as fp:
            CACHE = pickle.load(fp)
        return
    dump_cache()


class NewClient:

    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0

    def __real_get_access_token(self):
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
                   "client_credential&appid=%s&secret=%s" % (os.getenv('WECHAT_APP_ID', WECHAT_APP_ID), os.getenv('WECHAT_APP_SECRET', WECHAT_APP_SECRET)))
        urlResp = urllib.request.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())
        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']

    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
        return self.__accessToken


def Client():
    robot = WeRoBot()
    robot.config["APP_ID"] = os.getenv('WECHAT_APP_ID', WECHAT_APP_ID)
    robot.config["APP_SECRET"] = os.getenv(
        'WECHAT_APP_SECRET', WECHAT_APP_SECRET)
    # print(robot.config["APP_SECRET"])
    client = robot.client
    token = client.grant_token()
    return client, token


def cache_get(key):
    if key in CACHE:
        return CACHE[key]
    return None


def file_digest(file_path):
    """
    计算文件的md5值
    """
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        md5.update(f.read())
    return md5.hexdigest()


def cache_update(file_path):
    digest = file_digest(file_path)
    CACHE[digest] = "{}:{}".format(file_path, datetime.now())
    dump_cache()


def file_processed(file_path):
    digest = file_digest(file_path)
    return cache_get(digest) != None


def upload_image_from_path(image_path):
    image_digest = file_digest(image_path)
    res = cache_get(image_digest)
    if res != None:
        return res[0], res[1]
    client, _ = Client()
    media_json = client.upload_permanent_media(
        "image", open(image_path, "rb"))  # 永久素材
    media_id = media_json['media_id']
    media_url = media_json['url']
    CACHE[image_digest] = [media_id, media_url]
    dump_cache()
    print("file: {} => media_id: {}".format(image_path, media_id))
    return media_id, media_url


def upload_image(img_url):
    """
    * 上传临时素菜
    * 1、临时素材media_id是可复用的。
    * 2、媒体文件在微信后台保存时间为3天，即3天后media_id失效。
    * 3、上传临时素材的格式、大小限制与公众平台官网一致。
    """
    try:
        resource = urllib.request.urlopen(img_url)
    except URLError as e:
        print(f'Fail to upload pic:{img_url}')
        raise 'fail'

    name = img_url.split("/")[-1]
    f_name = "tmp_{}".format(name)
    if "." not in f_name:
        f_name = f_name + ".png"
    with open(f_name, 'wb') as f:
        f.write(resource.read())
    return upload_image_from_path(f_name)


def get_images_from_markdown(content):
    lines = content.split('\n')
    images = []
    for line in lines:
        line = line.strip()
        if line.startswith('![') and line.endswith(')'):
            image = line.split('(')[1].split(')')[0].strip()
            images.append(image)
    return images


def fetch_attr(content, key):
    """
    从markdown文件中提取属性
    """
    lines = content.split('\n')
    for line in lines:
        if line.startswith(key):
            return line.split(':')[1].strip()
    return ""


def render_markdown(content):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite', # markdown.extensions.fenced_code codehilite
            'markdown.extensions.tables', 'markdown.extensions.toc',
            'markdown.extensions.sane_lists', 'markdown.extensions.nl2br']
    post = "".join(content.split("---\n")[2:])
    html = markdown.markdown(post, extensions=exts)
    open("origin.html", "w").write(html)
    return css_beautify(html)


def update_images_urls(content, uploaded_images):
    for image, meta in uploaded_images.items():
        orig = "({})".format(image)
        new = "({})".format(meta[1])
        content = content.replace(orig, new)
    return content


def replace_para(content):
    new = """<p style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: rgb(89,89,89);">"""

    res = []
    for line in content.split("\n"):
        if line.startswith("<p>"):
            line = line.replace("<p>", new)
        res.append(line)
    return "\n".join(res)


def replace_header(content):
    res = []
    for line in content.split("\n"):
        l = line.strip()
        if l.startswith("<h") and l.endswith(">") > 0:
            tag = l.split(' ')[0].replace('<', '')
            value = l.split('>')[1].split('<')[0]
            digit = tag[1]
            font = (18 + (4 - int(tag[1])) *
                    2) if (digit >= '0' and digit <= '9') else 18
            new = "<{} style=\"margin-top: 30px; margin-bottom: 15px; padding: 0px; font-weight: bold; color: black; font-size: {}px;\"><span class=\"prefix\" style=\"display: none;\"></span><span class=\"content\">{}</span><span class=\"suffix\"></span></{}>".format(
                tag, font, value, tag)
            res.append(new)
        else:
            res.append(line)
    return "\n".join(res)


def replace_links(content):
    pq = PyQuery(open('origin.html').read())
    links = pq('a')
    refs = []
    index = 1
    if len(links) == 0:
        return content
    for l in links.items():
        new = "<span class=\"footnote-word\" style=\"color: #1e6bb8; font-weight: bold;\">{}</span><sup class=\"footnote-ref\" style=\"line-height: 0; color: #1e6bb8; font-weight: bold;\">[{}]</sup>".format(
            l.text(), index)
        index += 1
        refs.append([l.attr('href'), l.text(), new])

    for r in refs:
        orig = "<a href=\"{}\">{}</a>".format(r[0], r[1])
        content = content.replace(orig, r[2])
    content = content + "\n" + """<h3 class="footnotes-sep" style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-weight: bold; color: black; font-size: 20px;"><span style="display: block;">参考:</span></h3>\n"""
    content = content + """<section class="footnotes">"""
    index = 1
    for r in refs:
        l = r[2]
        line = "<span id=\"fn1\" class=\"footnote-item\" style=\"display: flex;\"><span class=\"footnote-num\" style=\"display: inline; width: 10%; background: none; font-size: 80%; opacity: 0.6; line-height: 26px; font-xxx: ptima-Regular, Optima, PingFangSC-light, PingFangTC-light, 'PingFang SC', Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;\">[{}] </span><p style=\"padding-top: 8px; padding-bottom: 8px; display: inline; font-size: 14px; width: 90%; padding: 0px; margin: 0; line-height: 26px; color: black; word-break: break-all; width: calc(100%-50);\">&nbsp{}: <em style=\"font-style: italic; color: black;\">{}</em></p>".format(index, r[
            1], r[0])
        index += 1
        content = content + line + "\n"
    content = content + "</section>"
    return content


def fix_image(content):
    pq = PyQuery(open('origin.html').read())
    imgs = pq('img')
    for line in imgs.items():
        link = """<img alt="{}" src="{}" />""".format(
            line.attr('alt'), line.attr('src'))
        caption = """\n<figcaption style="margin-top: 5px; text-align: center; color: #888; font-size: 14px;">{}</figcaption>\n""".format(
            line.attr('alt'))
        figure = """<figure style="margin: 0; margin-bottom: 5px; display: flex; flex-direction: column; justify-content: center; align-items: center;">""" + link + caption + "</figure>"
        content = content.replace(link, figure)
    return content

def format_code(content):
    content = content.replace("<code>", '<code style="font-size: 14px; word-wrap: break-word; padding: 2px 4px; border-radius: 4px; margin: 0 2px; background-color: rgba(27,31,35,.05); font-family: Operator Mono, Consolas, Monaco, Menlo, monospace; word-break: break-all; color: rgb(239, 112, 96);">')
    return content

def format_fix(content):
    content = content.replace("</li>\n<li>", "</li><li>")
    content = content.replace("<ul>\n<li>", "<ul><li>")
    content = content.replace("</li>\n</ul>", "</li></ul>")
    content = content.replace("<ol>\n<li>", "<ol><li>")
    content = content.replace("</li>\n</ol>", "</li></ol>")
    content = content.replace("class=\"codehilite\"",
                              "class=\"codehilite\" style=\"background-color: beige;\"")
    return content



def css_beautify(content):
    header = """<section id="nice" style="font-size: 16px; color: black; padding: 0 10px; line-height: 1.6; word-spacing: 0px; letter-spacing: 0px; word-break: break-word; word-wrap: break-word; text-align: left; font-xxx: Optima-Regular, Optima, PingFangSC-light, PingFangTC-light, 'PingFang SC', Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;">"""
    content = replace_para(content)
    content = replace_header(content)
    content = replace_links(content)
    content = format_code(content)
    content = format_fix(content)
    content = fix_image(content)
    content = header + content + "</section>"
    return content


def upload_media_news(post_path):
    """
    上传到微信公众号素材
    """
    content = open(post_path, 'r').read()
    TITLE = fetch_attr(content, 'title').strip('"').strip('\'')
    images = get_images_from_markdown(content)
    print(TITLE)
    print(images)
    if len(images) == 0:
        images.append('https://source.unsplash.com/random/600x400/?tech')
    uploaded_images = {}
    for image in images:
        media_id = ''
        media_url = ''
        if image.startswith("http"):
            media_id, media_url = upload_image(image)
        else:
            media_id, media_url = upload_image_from_path(
                "./blog-source/source" + image)
        uploaded_images[image] = [media_id, media_url]

    # 替换文章里面的图片
    content = update_images_urls(content, uploaded_images)

    THUMB_MEDIA_ID = (len(images) > 0 and uploaded_images[images[0]][0]) or ''
    AUTHOR = '叉叉敌'
    RESULT = render_markdown(content)
    # link = os.path.basename(post_path).replace('.md', '')
    digest = fetch_attr(content, 'subtitle').strip().strip('"').strip('\'')
    CONTENT_SOURCE_URL = 'https://chasays.github.io'

    articles = {
        'articles':
        [
            {
                "title": TITLE,
                "thumb_media_id": THUMB_MEDIA_ID,
                "author": AUTHOR,
                "digest": digest,
                "show_cover_pic": 1,
                "content": RESULT,
                # "content_source_url": CONTENT_SOURCE_URL,
                "need_open_comment": 1
            }
            # 若新增的是多图文素材，则此处应有几段articles结构，最多8段
        ]
    }
    with open('./result.html', 'w') as fp:
        fp.write(RESULT)
        fp.close()

    client = NewClient()
    token = client.get_access_token()
    headers = {'Content-type': 'text/plain; charset=utf-8'}
    datas = json.dumps(articles, ensure_ascii=False).encode('utf-8')

    postUrl = "https://api.weixin.qq.com/cgi-bin/draft/add?access_token=%s" % token
    r = requests.post(postUrl, data=datas, headers=headers)
    resp = json.loads(r.text)
    print(resp)
    media_id = resp['media_id']
    cache_update(post_path)
    return resp


def free_publish(m_id):

    client = NewClient()
    token = client.get_access_token()
    headers = {'Content-type': 'text/plain; charset=utf-8'}
    datas = json.dumps({'media_id': m_id}, ensure_ascii=False).encode('utf-8')

    postUrl = "https://api.weixin.qq.com/cgi-bin/freepublish/submit?access_token=%s" % token
    r = requests.post(postUrl, data=datas, headers=headers)
    resp = json.loads(r.text)
    print(resp)
    media_id = resp['publish_id']
    cache_update(media_id)
    return resp

def debug_generate_html(post_path):
    content = open(post_path, 'r').read()
    RESULT = render_markdown(content)
    with open('./result.html', 'w') as fp:
        fp.write(RESULT)
        fp.close()


def run(string_date):
    #string_date = "2022-02-04"
    print(string_date)
    pathlist = Path("./_posts/").glob('**/*.md')
    for path in pathlist:
        path_str = str(path)
        if file_processed(path_str):
            print("{} has been processed".format(path_str))
            continue
        if string_date in path.name:
            print(path_str)
            news_json = upload_media_news(path_str)
            print(news_json)
            print('successful')


if __name__ == '__main__':
    ## for debug
    # path_str = '_posts/2022/2022-05-02-LLVM-intrinsic_introduce.md'
    # debug_generate_html(path_str)
     
    init_cache()
    start_time = time.time()  # 开始时间
    times = [datetime.now(), datetime.now() - timedelta(days=1)]
    for x in times:
        print("start time: {}".format(x.strftime("%m/%d/%Y, %H:%M:%S")))
        string_date = x.strftime('%Y-%m-%d')
        print(string_date)
        run(string_date)
    end_time = time.time()  # 结束时间
    print("程序耗时%f秒." % (end_time - start_time))


