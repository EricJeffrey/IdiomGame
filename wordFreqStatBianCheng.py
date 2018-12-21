
# -*- coding:UTF-8 -*-

def readAllWords():
    fp = open("words.txt", "r", encoding="utf-8")
    res = []
    for line in fp.readlines():
        if len(line) is not 0:
            res.append(line[0])
    fp.close()
    return res

# sort a dict of key, value by value
def sortDictByValue(d, reverse):
    '''sort a dict by value, return tuple list of key, value'''
    ditems = d.items()
    tmpList = [(v[1], v[0]) for v in ditems]
    tmpList.sort(reverse=reverse)
    tmpList = [(v[1], v[0]) for v in tmpList]
    return tmpList

def work():
    words = {s:0 for s in readAllWords()}
    fp = open("BianCheng.txt", "r", encoding="utf-8")
    for line in fp.readlines():
        for word in line:
            if words.__contains__(word):
                words[word] += 1
    words = sortDictByValue(words, True)
    fp.close()
    fp = open("wordFreq.txt", "w", encoding="UTF-8")
    fp.writelines([(str(x) + "\n") for x in words])
    fp.close()

work()
