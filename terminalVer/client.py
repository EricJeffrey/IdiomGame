import threading


class Idiom():

    def __init__(self, desc=None, d=None, e=None, p=None):
        self.desc = desc
        self.deri = d
        self.expl = e
        self.pinyin = p


class IdiomPair():

    def __init__(self, keyWord=None, rpos=0, cpos=0, eightWords=None, firstIdiom=None, secondIdiom=None):
        self.keyWord = keyWord
        self.cpos = cpos
        self.rpos = rpos
        self.eightWords = eightWords
        self.first = firstIdiom
        self.second = secondIdiom


class IdiomGameClient():

    def __init__(self):
        self.CODE_GET_ROUND_DATA = 101
        self.CODE_EXIT = 10
        self.CODE_WIN = 11
        self.CODE_IDIOM_DETAIL = 12
        self.CODE_NEXT_ROUND = 13
        self.ROUND_REQUEST_SENT = False
        self.ROUND_DATA_REFRESHED = False
        self.ROUND_DATA = IdiomPair()
        self.ROUND_NUM = 1

    def start(self):
        while (True):
            # send data if not sent
            if not self.ROUND_REQUEST_SENT:
                self.getRoundDataAsync(self.ROUND_NUM)
                self.ROUND_REQUEST_SENT = True
            # check whether we have got data
            if self.ROUND_DATA_REFRESHED:
                # show it
                self.showData()
                anwser = self.checkInputAnwser()
                # if player wins
                if anwser == self.CODE_WIN:
                    ansAfterWin = self.winWork()
                    # if player wants to see idiom detail
                    if ansAfterWin == self.CODE_IDIOM_DETAIL:
                        self.showIdiomDetail()
                        ansAfterDetail = self.checkInputAfterDetail()
                        # if player wants to exit
                        if ansAfterDetail == self.CODE_EXIT:
                            exit()
                        # if go on, do some clear and it will go on looping
                        elif ansAfterDetail == self.CODE_NEXT_ROUND:
                            self.workAfterWin()
                    elif ansAfterWin == self.CODE_EXIT:
                        exit()
                    elif ansAfterWin == self.CODE_NEXT_ROUND:
                        self.workAfterWin()
                        pass
                elif anwser == self.CODE_EXIT:
                    exit()

    def showData(self):
        roundData = self.ROUND_DATA
        fw = roundData.first.desc
        sw = roundData.second.desc
        rpos = roundData.rpos
        cpos = roundData.cpos
        # set data into it
        tmps = ""
        for i in range(4):
            if i == rpos:
                for j in range(4):
                    if j == cpos:
                        tmps += "  "
                    else:
                        tmps += fw[j]
            else:
                for j in range(4):
                    if j == cpos:
                        tmps += sw[i]
                    else:
                        tmps += "  "
            tmps += "\n"
        print(tmps)

        # construct matrix
        # matrix = []
        # for i in range(0, 4):
        #     matrix.append([])
        #     tmpn = 7
        #     if i == roundData.rpos:
        #         tmpn = 5
        #     while tmpn > 0:
        #         matrix[i].append(' ')
        #         tmpn -= 1
        # for i in range(0, 4):
        #     if i != cpos:
        #         matrix[rpos][i] = fw[i]
        #     if i != rpos:
        #         matrix[i][cpos * 2] = sw[i]
        # matrix[rpos][cpos * 2] = matrix[rpos][cpos * 2 + 1] = ' '
        # tmps = ""
        # for i in range(0, len(matrix)):
        #     for j in range(0, len(matrix[i])):
        #         tmps += matrix[i][j]
        #     tmps += "\n"
        # print(tmps)
        tmps = ""
        for x in roundData.eightWords:
            tmps += x + " "
        print(tmps)

    def checkInputAnwser(self):
        while True:
            userSelectNum = input(
                "\nInput word number (from 1) and press enter, -1 to Exit: ")
            try:
                ind = int(userSelectNum) - 1
                rndData = self.ROUND_DATA
                if ind >= 0 and ind <= 7:
                    if rndData.eightWords[ind] == rndData.keyWord:
                        return self.CODE_WIN
                    else:
                        print("\nWrong Anwser emmmm, Try Again~\n")
                elif ind == -2:
                    return self.CODE_EXIT
                else:
                    print("\nWrong Input emmmm, Try Again~\n")
            except ValueError:
                print("\nWrong Input emmmm, Try Again~\n")

    def showIdiomDetail(self):
        rndData = self.ROUND_DATA
        first = rndData.first
        second = rndData.second
        lf = "\n"
        deri = "出处:"
        expl = "释义:"
        piny = "拼音:"
        firs = first.desc + ":" + lf + deri + first.deri + \
            lf + expl + first.expl + lf + piny + first.pinyin
        secs = second.desc + ":" + lf + deri + second.deri + \
            lf + expl + second.expl + lf + piny + second.pinyin
        print(firs + lf + secs)
        pass

    def checkInputAfterDetail(self):
        while True:
            inputAfterDetail = input(
                "\nInput 1 to Next Round, -1 to Exit: ")
            try:
                num = int(inputAfterDetail)
                if num == 1:
                    return self.CODE_NEXT_ROUND
                elif num == -1:
                    return self.CODE_EXIT
                else:
                    print("Input Wrong, Try Again~")
            except ValueError:
                print("Input Wrong, Try Again~")

    def winWork(self):
        numAfterWin = input(
            "Congratulations! You have won this round.\nInput 1 to Next Round, 2 Show Idiom Detail -1 to Exit: ")
        while(True):
            try:
                num = int(numAfterWin)
                if num == 1:
                    return self.CODE_NEXT_ROUND
                elif num == 2:
                    return self.CODE_IDIOM_DETAIL
                elif num == -1:
                    return self.CODE_EXIT
                else:
                    print("\nWrong Input, Try Again~\n")
                    numAfterWin = input()
            except ValueError:
                print("\nWrong Input, Try Again~\n")
                numAfterWin = input()
                continue

    def workAfterWin(self):
        self.ROUND_NUM += 1
        self.ROUND_REQUEST_SENT = False
        self.ROUND_DATA_REFRESHED = False

    def getRoundData(self, roundNum):
        with open("terminalVer/goodIdiomPair.txt", "r", encoding="UTF-8") as fp:
            n = roundNum
            line1 = line2 = ""
            while n > 0:
                line1 = fp.readline()
                line2 = fp.readline()
                n -= 1
            lineli1 = line1.split("\t")
            lineli2 = line2.split("\t")
            posli = lineli1[1].split(',')
            rpos = int(posli[0])
            cpos = int(posli[1])
            eightWords = lineli1[2].split(',')
            first = Idiom(lineli1[3], lineli1[4], lineli1[5], lineli1[6])
            second = Idiom(lineli2[0], lineli2[1], lineli2[2], lineli2[3])
            self.ROUND_DATA = IdiomPair(
                lineli1[0], rpos, cpos, eightWords, first, second)
            self.ROUND_DATA_REFRESHED = True

    def getRoundDataAsync(self, roundNum):
        # new thread get data
        threading.Thread(target=self.getRoundData(roundNum)).start()


if __name__ == "__main__":
    IdiomGameClient().start()
