# -*- coding:UTF-8 -*-

import urllib
import urllib.request

def readOldWordsDict():
    allWords = {}
    wordFreqFp = open("wordsFreqNews.txt", "r")
    tmpLine = wordFreqFp.readline()
    while len(tmpLine) > 0:
        tmpTuple = tuple(tmpLine.strip().split(','))
        allWords[tmpTuple[0]] = int(tmpTuple[1])
        tmpLine = wordFreqFp.readline()
    wordFreqFp.close()
    return allWords

# read new data and update freq
def updateFreq(host, allWordsDict):
    res = urllib.request.urlopen(host, data=None, timeout=10)
    data = res.read().decode()
    for ch in data:
        if allWordsDict.__contains__(ch):
            allWordsDict[ch] += 1
    return allWordsDict


# sort a dict of key, value by value
def sortDictByValue(d, reverse):
    '''sort a dict by value, return tuple list of key, value'''
    ditems = d.items()
    tmpList = [(v[1], v[0]) for v in ditems]
    tmpList.sort(reverse=reverse)
    tmpList = [(v[1], v[0]) for v in tmpList]
    return tmpList


# write freq to file
def writeFreq(wordsFreqList):
    wfn = open("wordsFreqNews.txt", "w")
    for x in wordsFreqList:
        wfn.write(str(x[0]))
        wfn.write(',' + str(x[1]) + "\n")


def work(host):
    wordsDict = readOldWordsDict()
    wordsDict = updateFreq(host, wordsDict)
    wordsFreqList = sortDictByValue(wordsDict, True)
    writeFreq(wordsFreqList)


work("http://www.people.com.cn/rss/finance.xml")
