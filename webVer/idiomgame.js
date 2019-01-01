
var gtbody, atbody, dtbody;
var ansbtn;
var windialogdiv;
var ansShown = false, detailShown = false, winDialogShown = false;

var roundNum;
var rounddata;

// 清除旧数据
function clearOldData(gametbody, anstbody, detailtbody) {
    var childnodes = gametbody.childNodes;
    for (var i = 0; i < 3; i++) {
        var tmpbody = gametbody;
        if (i == 1)
            tmpbody = anstbody;
        if (i == 2)
            tmpbody = detailtbody;
        var childnodes = tmpbody.childNodes;
        for (var j = childnodes.length - 1; j > 0; j--)
            tmpbody.removeChild(childnodes[j]);
    }
    windialogdiv.style.visibility = "hidden";
    detailtbody.style.visibility = "hidden";
    ansShown = detailShown = winDialogShown = false;
}

// pri 添加一个2*4的表格展示候选字
function priShowAnsData(eightWords, anstbody) {
    for (var i = 0; i < 2; i++) {
        var tmptr = document.createElement("tr");
        for (var j = 0; j < 4; j++) {
            var tmptd = document.createElement("td");
            var tmpbtn = document.createElement("button");
            tmpbtn.setAttribute("class", "ans_word_btn");
            tmpbtn.innerText = eightWords[i * 4 + j];
            tmpbtn.addEventListener("click", checkAnwserListener);
            tmptd.appendChild(tmpbtn);
            tmptr.appendChild(tmptd);
        }
        anstbody.appendChild(tmptr);
    }
}

// pri 添加一个4*4的表格展示成语里面的字
function priShowIdiomData(rpos, cpos, fw, sw, gametbody) {
    for (var i = 0; i < 4; i++) {
        var tmptr = document.createElement("tr");
        for (var j = 0; j < 4; j++) {
            var tmptd = document.createElement("td");
            if (i == rpos && j != cpos) {
                var tmpbtn = document.createElement("button");
                tmpbtn.setAttribute("class", "idiom_btn");
                tmpbtn.innerText = fw[j];
                tmptd.appendChild(tmpbtn);
            }
            if (j == cpos && i != rpos) {
                var tmpbtn = document.createElement("button");
                tmpbtn.setAttribute("class", "idiom_btn");
                tmpbtn.innerText = sw[i];
                tmptd.appendChild(tmpbtn);
            }
            if (i == rpos && j == cpos) {
                var tmpbtn = document.createElement("button");
                tmpbtn.setAttribute("class", "idiom_ans_btn");
                tmpbtn.setAttribute("style", "background:#ffdd11;")
                tmptd.appendChild(tmpbtn);
                ansbtn = tmpbtn;
            }
            tmptr.appendChild(tmptd);
        }
        gametbody.appendChild(tmptr);
    }
}

// 刷新关卡数据
function refreshRoundData() {
    if (gtbody == null)
        gtbody = document.getElementById("gametbody");
    if (atbody == null)
        atbody = document.getElementById("anstbody");
    if (dtbody == null)
        dtbody = document.getElementById("detailtbody");
    if (windialogdiv == null)
        windialogdiv = document.getElementById("windialogdiv");
    clearOldData(gtbody, atbody, dtbody);
    var rpos = rounddata.rpos, cpos = rounddata.cpos;
    var fw = rounddata.first.desc, sw = rounddata.second.desc;
    priShowIdiomData(rpos, cpos, fw, sw, gtbody);
    var eightWords = rounddata.eightWords;
    priShowAnsData(eightWords, atbody);
}

// 更改通关对话框可见性
function toggleWinDialog() {
    bottomdiv = document.getElementById("bottom_div");
    if (winDialogShown) {
        windialogdiv.style.visibility = "hidden";
        bottomdiv.style.filter = "none";
        bottomdiv.style.pointerEvents = "all";
    } else {
        windialogdiv.style.visibility = "visible";
        bottomdiv.style.filter = "blur(2px)";
        bottomdiv.style.pointerEvents = "none";
    }
    winDialogShown = !winDialogShown;
}

// 检查答案是否正确
function checkAnwserListener(event) {
    if (event.target.innerText == rounddata.keyword) {
        if (!ansShown) {
            showAns();
            toggleWinDialog();
        }
    }
    else {
        alert("答错了");
        // todo 震动
    }
}

// 进入下一关
function goNextRound() {
    updateUserRound(() => {
        getNextRoundData((data, textStatus, jqxhr) => {
            console.log(data);
            console.log(textStatus);
            rounddata = JSON.parse(data);
            refreshRoundData();
        });
    });
}

// 更新用户通关数据
function updateUserRound(success) {
    $.post("/idiomgameupdatauserrnd", { roundNum: roundNum }, success);
}

// 获取下一关数据
function getNextRoundData(success) {
    roundNum += 1;
    $.get("/idiomgamerounddata", { roundNum: roundNum }, success);
}

// 显示网络错误
function showNetworkError() {
    alert("连接超时，请检查网络连接并刷新页面");
}

// 显示答案
function showAns() {
    if (ansShown)
        return;
    document.getElementById("nextrndbtn").style.display = "initial";
    ansShown = true;
    ansbtn.innerText = rounddata.keyword;
}

// 显示释义
function showIdiomDetail(dtbody) {
    if (detailShown)
        return;
    if (winDialogShown)
        toggleWinDialog();
    detailShown = true;
    showAns();
    dtbody.style.visibility = "visible";
    for (var i = 0; i < 2; i++) {
        var tmpidiom = rounddata.first;
        if (i == 1)
            tmpidiom = rounddata.second;
        var deri = "出处", expl = "释义", pinyin = "拼音";
        var tmptds = new Array(7);
        var values = [tmpidiom.desc, deri, tmpidiom.deri, expl, tmpidiom.expl, pinyin, tmpidiom.pinyin];
        for (var j = 0; j < 7; j++) {
            tmptds[j] = document.createElement("td");
            tmptds[j].innerText = values[j];
            tmptds[j].setAttribute("class", "idiom_detal_td");
        }
        var tmptr = document.createElement("tr");
        tmptds[0].setAttribute("colspan", "2");
        tmptds[0].setAttribute("style", "font-weight:bold;");
        tmptr.appendChild(tmptds[0]);
        dtbody.appendChild(tmptr);
        for (j = 1; j < 7; j += 2) {
            tmptr = document.createElement("tr");
            tmptr.appendChild(tmptds[j]);
            tmptr.appendChild(tmptds[j + 1]);
            dtbody.appendChild(tmptr);
        }
    }
}

window.onload = function () {
        /*todo 服务端设置值*/roundNum = 1;
        /*todo 服务端设置值*/rounddata = {
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
    refreshRoundData();
}