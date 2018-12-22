
import json
import random
'''
*********************************************************************************
# part 0 -- test part
*********************************************************************************
'''


def freqIdiomTest():
    idioms = inIdioms()
    s = set()
    with open("terminalVer/test.out", "w", encoding="UTF-8") as fp:
        for idiom in idioms:
            if idiom in s:
                fp.write(idiom)
                fp.write("\n")
            s.add(idiom)


'''
*********************************************************************************
# part 1 -- create pairs
*********************************************************************************
'''

def createMap(idioms):
    word2idioms = {}
    for idiom in idioms:
        tmpWordSet = set()
        for word in idiom:
            if not word2idioms.__contains__(word):
                word2idioms[word] = []
            if word not in tmpWordSet:
                word2idioms[word].append(idiom)
                tmpWordSet.add(word)
    return word2idioms


def createIdiomPairs(word2idioms):
    visitedIdioms = set()
    idiomPairs = []
    for key in word2idioms.keys():
        tmpIdioms = word2idioms[key]
        tmpUnvisitedIdioms = []
        for idiom in tmpIdioms:
            if idiom not in visitedIdioms:
                tmpUnvisitedIdioms.append(idiom)
        tmplen = len(tmpUnvisitedIdioms)
        if tmplen <= 1:
            continue
        for i in range(1, tmplen, 2):
            if i >= tmplen:
                break
            a = tmpUnvisitedIdioms[i - 1]
            b = tmpUnvisitedIdioms[i]
            # if a in visitedIdioms or b in visitedIdioms:
            #     i += 1
            #     continue
            idiomPairs.append(
                (key, (tmpUnvisitedIdioms[i - 1], tmpUnvisitedIdioms[i])))
            visitedIdioms.add(a)
            visitedIdioms.add(b)
    return idiomPairs


def inIdioms():
    freqIdioms = open("terminalVer/freqIdioms.txt", "r", encoding="UTF-8")
    idioms = []
    for line in freqIdioms.readlines():
        idioms.append(line.strip("\n"))
    freqIdioms.close()
    return idioms


def outIdiomPairs(idiomPairs):
    idiomPairsFp = open("terminalVer/data.out", "w", encoding="UTF-8")
    for p in idiomPairs:
        idiomPairsFp.write(str(p) + "\n")
    idiomPairsFp.close()
    pass


def createRawDataWork():
    idioms = inIdioms()
    word2idioms = createMap(idioms)
    idiomPairs = createIdiomPairs(word2idioms)
    outIdiomPairs(idiomPairs)

# createRawDataWork()

'''
*********************************************************************************
# part 2 -- create useful data with structure:
*********************************************************************************
'''

class Idiom():

    def __init__(self, desc=None, d=None, e=None, p=None):
        self.desc = desc
        self.deri = d
        self.expl = e
        self.pinyin = p


class IdiomPair():

    def __init__(self, keyWord, firstWord=None, secondWord=None):
        self.keyWord = keyWord
        self.first = None
        self.second = None
        self.firstWord = firstWord
        self.secondWord = secondWord
        self.cpos = -1
        self.rpos = -1
        self.eightWords = None
        self.cacuPos()

    def cacuPos(self):
        for i in range(4):
            if self.firstWord[i] == self.keyWord:
                self.cpos = i
                break
        for i in range(4):
            if self.secondWord[i] == self.keyWord:
                self.rpos = i
                break
        pass
    
    def setData(self, firDeri, firExpl, firPy, secDeri, secExpl, secPy, eightWords):
        self.first  = Idiom(self.firstWord, firDeri, firExpl, firPy)
        self.second = Idiom(self.secondWord, secDeri, secExpl, secPy)
        self.eightWords = eightWords
        return self
    
    def toStr(self):
        spli = "\t"
        fir = self.first
        sec = self.second
        pos = "(" + str(self.rpos) + "," + str(self.cpos) + ")"
        wordstr = ""
        for word in self.eightWords:
            wordstr += word
            wordstr += ","
        wordstr = wordstr.strip(",")
        res = self.keyWord + spli + pos + spli + wordstr
        res += spli +  fir.desc + spli + fir.deri + spli + fir.expl + spli + fir.pinyin + "\n"
        res += 3 * spli + sec.desc + spli +sec.deri + spli + sec.expl + spli + sec.pinyin + "\n"
        return res


  
# {
#     "derivation": "语出《法华经·法师功德品》下至阿鼻地狱。”",
#     "example": "但也有少数意志薄弱的……逐步上当，终至堕入～。★《上饶集中营·炼狱杂记》",
#     "explanation": "阿鼻梵语的译音，意译为无间”，即痛苦无有间断之意。常用来比喻黑暗的社会和严酷的牢狱。又比喻无法摆脱的极其痛苦的境地。",
#     "pinyin": "ā bí dì yù",
#     "word": "阿鼻地狱",
#     "abbreviation": "abdy"
# },

def readIdiomDict():
    idioms = json.load(open("idiom.json", "r", encoding="UTF-8"))
    idiomDict = {}
    for idiom in idioms:
        idiomDict[idiom["word"]] = {"deri":idiom["derivation"], "expl": idiom["explanation"], "pinyin": idiom["pinyin"]}
    return idiomDict

def readPairData():
    with open("terminalVer/idiomPairRaw.txt", "r", encoding="UTF-8") as fp:
        idiomPairsRaw = [(s.strip("\n").split(',')) for s in fp.readlines()]
        idiomPairs = []
        for rawPair in idiomPairsRaw:
            idiomPairs.append(IdiomPair(rawPair[0], firstWord=rawPair[1], secondWord=rawPair[2]))
    return idiomPairs

def readWordsList():
    with open("terminalVer/freqWords.txt", "r", encoding="UTF-8") as fp:
        wordsList = [s.strip("\n") for s in fp.readlines()]
    return wordsList

def getEightWords(keyWord, wordsList):
    rinds = random.sample(wordsList, 8)
    eightWords = []
    n = 0
    for x in rinds:
        if x != keyWord:
            eightWords.append(x)
            n += 1
        if n == 7:
            break
    eightWords.append(keyWord)
    random.shuffle(eightWords)
    return eightWords

def createCompleteData(idiomDict, idiomPairs, wordsList):
    compPairData = []
    for p in idiomPairs:
        fd = idiomDict[p.firstWord]
        sd = idiomDict[p.secondWord]
        compPairData.append(p.setData(fd["deri"], fd["expl"], fd["pinyin"], sd["deri"], sd["expl"], sd["pinyin"], getEightWords(p.keyWord, wordsList)))
    return compPairData

def completeDataWork():
    compPairData = createCompleteData(readIdiomDict(), readPairData(), readWordsList())
    random.shuffle(compPairData)
    with open("terminalVer/idiomPairTxt_word_deri_expl_py.out", "w", encoding="UTF-8") as fp:
        for i in range(0, len(compPairData)):
            tmpPair = compPairData[i]
            fp.write(tmpPair.toStr())
        fp.close()

completeDataWork()

'''
*********************************************************************************
# part 3 -- clean freaqIdioms data
*********************************************************************************
'''
def cleanData():
    with open("terminalVer/freqIdioms.txt", "r", encoding="UTF-8") as fp:
        idioms = [s.strip("\n") for s in fp.readlines()]
        detailedIdioms = json.load(open("idiom.json", "r+", encoding="UTF-8"))
        allIdiomSet = set()
        for didiom in detailedIdioms:
            allIdiomSet.add(didiom["word"])
        idiomsLen = len(idioms)
        for i in range(idiomsLen - 1, -1, -1):
            tmpidiom = idioms[i]
            if tmpidiom not in allIdiomSet:
                idioms.remove(tmpidiom)
        cleandFp = open("terminalVer/cleanedFreqIdioms.txt", "w", encoding="UTF-8")
        cleandFp.writelines([s + "\n" for s in idioms])
        cleandFp.close()

# cleanData()


'''
*********************************************************************************
# part 4 -- create words data
*********************************************************************************
'''

def createWordsFromFreqIdioms():
    words = None
    with open("terminalVer/freqIdioms.txt", "r", encoding="UTF-8") as fp:
        wordsSet = set()
        idioms = [s.strip("\n") for s in fp.readlines()]
        for idiom in idioms:
            for x in idiom:
                wordsSet.add(x)
        words = [x+"\n" for x in wordsSet]
    with open("terminalVer/freqWords.txt", "w", encoding="UTF-8") as fp:
        fp.writelines(words)

# createWordsFromFreqIdioms()
    
        
