#coding: utf-8
import sys

def makeFeatureList():
    #素性番号1(配列のインデックス0番)は"未定義語"
    features=["未定義"]

    for line in open('./data/train_kakaku.txt', 'r'):
        for w in line.rstrip("\n").split(" ")[1:]:
            if w in features:
                pass
            else:
                features.append(w)

    return features

# featureリストと一行のラベル, 単語列を引数として、文字列を返す
def libsvmFormat(features, line):
    unknown = 0
    lst = line.split(" ")
    label = lst[0]
    words = lst[1:]
    ans = [label]

    f = {}
    for w in words:
        if w in features:
            ind = features.index(w)
        else:
            ind = unknown

        if ind in f:
            f[ind] += 1
        else:
            f[ind] = 1

    for ind, cnt in f.items():
        s = "".join([" ", str(ind+1), ":", str(cnt)])
        ans.append(s)
        
    return "".join(ans)

if __name__ == '__main__':
    features=makeFeatureList()

    for line in sys.stdin:
        l = line.rstrip("\n")
        print libsvmFormat(features, l)
