# -*- coding:UTF-8-*-
# 提取所有长度为4的成语，统计所有字符的出现频率，选择出现频率较高的 N 个字

import json

# Load data
jsonArray = json.load(open("idiom.json", "r", encoding="UTF-8"))
for i in range(0, len(jsonArray)):
        jsonArray[i] = jsonArray[i]['word']


idiomArray = jsonArray.copy()
# statistics of word frequency
s = {}
for x in idiomArray:
    for c in x:
        if s.__contains__(c):
            s[c] += 1
        else:
            s[c] = 1

# get a word -> freq tuple array
sitems = s.items()
revItems = [(v[1], v[0]) for v in sitems]
revItems.sort(reverse = True)
sitems = [(v[1], v[0]) for v in revItems]

# save idiom frequency
wordFreqFile = open("wordFreq.txt", "w", encoding="UTF-8")
for x in sitems:
    _ = wordFreqFile.write(x[0])
    _ = wordFreqFile.write('\n')

wordFreqFile.flush()
wordFreqFile.close()

# remove long or short(not len of 4) idiom
l = len(idiomArray)
for i in range(l - 1, 0, -1):
    if len(idiomArray[i]) != 4:
        del idiomArray[i]

# save long short idiom
# idiomArray = jsonArray.copy()
# longShortIdiom = open("longShortIdiom.txt", "w")
# l = len(idiomArray)
# for i in range(l - 1, 0, -1):
#     if len(idiomArray[i]) != 4:
#         longShortIdiom.write(idiomArray[i])
#         longShortIdiom.write("\n")
# 
# 
# longShortIdiom.close()

# remove 
for i in range(l - 1, 0, -1):
    if len(idiomArray[i]) != 4:
        del idiomArray[i]

# statistics of idiom freq using word freq
idiomWordFreq = []
for x in idiomArray:
    if len(x) != 4:
        continue
    freq = 0
    tmps = {}
    for c in x:
        if not tmps.__contains__(c):
            freq += s[c]
            tmps[c] = 1
    idiomWordFreq.append(freq)

# write to idiom freq to file
testFp = open("testStat.txt", "w")
wordFreqArray = []
idiomArrayLen = len(idiomArray)
for i in range(0, idiomArrayLen):
    wordFreqArray.append((idiomWordFreq[i], idiomArray[i]))

wordFreqArray.sort(reverse = True)
wordFreqArray = [(v[1], v[0]) for v in wordFreqArray]
for x in wordFreqArray:
    testFp.write(str(x))
    testFp.write("\n")


testFp.close()

