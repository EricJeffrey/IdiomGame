# -*- coding: UTF-8 -*-

# transfer idiom.json -> {idiom, derivation, explanation, pinyin}
# "derivation": "语出《法华经·法师功德品》下至阿鼻地狱。”",
# "explanation": "阿鼻梵语的译音，意译为无间”，即痛苦无有间断之意。常用来比喻黑暗的社会和严酷的牢狱。又比喻无法摆脱的极其痛苦的境地。",
# "pinyin": "ā bí dì yù",
# "word": "阿鼻地狱",
import json

idioms = json.load(open("idiom.json", "r", encoding="UTF-8"))
outfp = open("/freshman/formattedIdiomsData.in", "w", encoding="UTF-8")
for idiom in idioms:
    spl = "\t"
    word = idiom["word"]
    deri = idiom["derivation"]
    py = idiom["pinyin"]
    expla = idiom["explanation"]
    outfp.write(word + spl + deri + spl + expla + spl + py + "\n")

outfp.close()
