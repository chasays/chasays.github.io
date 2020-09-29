# bubble
def bubble(list1):
    tmpLen = len(list1)
    for i in range(tmpLen):
        for j in range(1, tmpLen - i):
            if list1[j] < list1[j-1]:
                list1[j], list1[j-1] = list1[j-1], list1[j]
                print(i, j, list1)
    return list1


# 找出字符串中第一个不重复的字符
def findFirstAlpha(s):
    tmps = []
    for i in range(len(s)):
        print(tmps)
        if s[i] not in s[:i]:
            tmps.append(s[i])
        else:
            tmps.remove(s[i])
    ret = tmps[0] if len(tmps) else None
    print(ret)
    return ret
        
if __name__ == "__main__":
    tmplist = [5, 4, 3, 2, 1]
    # print(bubble((tmplist)))
    s = '1234123'
    findFirstAlpha(s)
        


