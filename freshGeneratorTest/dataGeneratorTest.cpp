#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;

typedef char WORD;
typedef string IDIOM;

map<WORD, VI> createMap(const vector<IDIOM> &idioms) {
    map<WORD, VI> word2IdiomInd;
    for (int i = 0; i < (int)idioms.size(); i++) {
        for (int j = 0; j < (int)idioms[i].size(); j++) {
            word2IdiomInd[idioms[i][j]].push_back(i);
        }
    }
    return word2IdiomInd;
}

vector<PII> createIdiomPairs(const vector<IDIOM> &idioms) {
    map<WORD, VI> word2IdiomInd = createMap(idioms);
    set<int> visitedIdiomInd;
    vector<PII> idiomPairs;
    map<WORD, VI>::iterator it = word2IdiomInd.begin();
    for (; it != word2IdiomInd.end(); it++) {
        VI idiomInds = it->second;
        VI tmpIdiomInds;
        for (int i = 0; i < (int)idiomInds.size(); i++) {
            int tmpInd = idiomInds[i];
            if (visitedIdiomInd.find(tmpInd) == visitedIdiomInd.end())
                tmpIdiomInds.push_back(tmpInd);
        }
        if (tmpIdiomInds.size() > 1) {
            for (int i = 1; i < (int)tmpIdiomInds.size(); i += 2) {
                int inda = tmpIdiomInds[i - 1], indb = tmpIdiomInds[i];
                visitedIdiomInd.insert(inda);
                visitedIdiomInd.insert(indb);
                idiomPairs.push_back(PII(inda, indb));
            }
        }
    }
    return idiomPairs;
}

int work() {
    // vector<IDIOM> idioms = {"兵强马壮", "马首是瞻", "精兵强将", "强能健体",
    // "首当其冲"};
    vector<IDIOM> idioms = {"abcd", "cefg", "habi", "bjkl", "emno"};
    vector<PII> idiomPairs = createIdiomPairs(idioms);
    for (PII p : idiomPairs) {
        int a = p.first, b = p.second;
        cout << idioms[a] << ' ' << idioms[b] << endl;
    }
    return 0;
}

void test() {
    string s = "兵强马壮";
    for (int i = 0; i < s.size(); i++) {
        cout << s[i] << endl;
    }
}
int main(int argc, char const *argv[]) {
    test();
    return 0;
}
