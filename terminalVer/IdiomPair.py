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

