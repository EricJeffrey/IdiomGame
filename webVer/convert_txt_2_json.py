

'''
{
        "keyword": "马",
        "rpos": 2,
        "cpos": 2,
        "eightWords": ["走", "开", "尽", "仰", "言", "老", "马", "虫"],
        "first": {
            "desc": "猴年马月",
            "deri": "无",
            "expl": "猴、马十二生肖之一。泛指未来的岁月。",
            "pinyin": "hóu nián mǎ yuè"
        },
        "second": {
            "desc": "兵强马壮",
            "deri": "《新五代史·安重荣传》尝谓人曰‘天子宁有种耶？兵强马壮者为之尔。’”",
            "expl": "兵力强盛，战马健壮。形容军队实力强，富有战斗力。",
            "pinyin": "bīng qiáng mǎ zhuàng"
        }
    };
'''
import json

rawfp = open("rawdata.txt", "r", encoding="utf-8")
outputfp = open("data.out", "w", encoding="utf-8")
outputdata = []
while True:
    tmpline1 = rawfp.readline()
    if len(tmpline1) == 0:
        break
    tmpline2 = rawfp.readline()
    tmplineli = tmpline1.split('\t')
    keyword = tmplineli[0]
    pos = tmplineli[1]
    posli = pos.split(',')
    rpos = posli[0]
    cpos = posli[1]
    eightWords = tmplineli[2]
    eightWords = eightWords.split(',')
    fwdesc = tmplineli[3]
    fwderi = tmplineli[4]
    fwexpl = tmplineli[5]
    fwpinyin = tmplineli[6]
    tmplineli = tmpline2.split('\t')
    swdesc = tmplineli[0]
    swderi = tmplineli[1]
    swexpl = tmplineli[2]
    swpinyin = tmplineli[3]
    tmppair = {
        "keyword": keyword,
        "rpos": rpos,
        "cpos": cpos,
        "eightWords": eightWords,
        "first": {
            "desc": fwdesc,
            "deri": fwderi,
            "expl": fwexpl,
            "pinyin": fwpinyin
        },
        "second": {
            "desc": swdesc,
            "deri": swderi,
            "expl": swexpl,
            "pinyin": swpinyin
        }
    }
    outputdata.append(tmppair)
json.dump(outputdata, outputfp, ensure_ascii=False)
rawfp.close()
outputfp.close()
