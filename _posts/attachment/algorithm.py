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
        
def isCardStraight(cards):
    tmpCards = [0] * 10 ## todo JQK
    if not isinstance(cards, list) or len(cards) != 5:
        raise ValueError("please correct cards value")
    for card in cards:
        tmpCards[card-1] = card
    print(tmpCards)
    for i, v in enumerate(tmpCards):
        print(i, v)
        if v != 0 and i < 6 and 0 not in tmpCards[i:i+5]: # out of list
                return True
    return False

def isStraight(cards):
    if 1 in cards and 13 in cards:
        cards[cards.index(1)]=14
    if 3 == sum(set([abs(x-sum(cards)/5) for x in cards])):
        return True
    else:
        return False


if __name__ == "__main__":
    tmplist = [5, 4, 3, 2, 1]
    tmplist = [11, 10, 12, 13, 1]
    # print(bubble((tmplist)))
    # s = '1234123'
    # findFirstAlpha(s)
    # print(isCardStraight(tmplist))
    print(isStraight(tmplist))
        


