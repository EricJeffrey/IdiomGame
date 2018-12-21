# -*- coding:UTF-8 -*-

# generate data
# Done target 1 -> create idiom pairs
# target 2 -> create idiom pairs with {explanation, origin, pinyin}

# pseudo code:

def createMap(idioms):
    word2idioms = {}
    for idiom in idioms:
        for word in idiom:
            if not word2idioms.__contains__(word):
                word2idioms[word] = []
            word2idioms[word].append(idiom)
    return word2idioms


def createIdiomPairs(word2idioms):
    visitedIdioms = set()
    idiomPairs = []
    for key in word2idioms.keys():
        tmpIdioms = word2idioms[key]
        tmpUnvisitedIdioms = []
        for idiom in tmpIdioms:
            if not visitedIdioms.__contains__(idiom):
                tmpUnvisitedIdioms.append(idiom)
        if len(tmpUnvisitedIdioms) <= 1:
            continue
        for i in range(1, len(tmpUnvisitedIdioms)):
            a = tmpUnvisitedIdioms[i - 1]
            b = tmpUnvisitedIdioms[i]
            idiomPairs.append((tmpUnvisitedIdioms[i - 1], tmpUnvisitedIdioms[i]))
            visitedIdioms.add(a)
            visitedIdioms.add(b)
            i += 2
    return idiomPairs


def inIdioms():
    word4idiomsfp = open("generatedData/word4idioms.txt", "r", encoding="UTF-8")
    idioms = []
    for line in word4idiomsfp.readlines():
        idioms.append(line.strip("\n"))
    word4idiomsfp.close()
    return idioms

def outIdiomPairs(idiomPairs):
    idiomPairsFp = open("data.out", "w", encoding="UTF-8")
    for p in idiomPairs:
        idiomPairsFp.write(str(p) + "\n")
    idiomPairsFp.close()
    pass

def work():
    idioms = inIdioms()
    word2idioms = createMap(idioms)
    idiomPairs = createIdiomPairs(word2idioms)
    outIdiomPairs(idiomPairs)

work()