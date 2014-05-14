#coding: utf-8
import sys

def makeFeatureList(train_file = './data/train_kakaku.txt'):
    #素性番号1(配列のインデックス0番)は"未知語"
    features=["未知語"]

    for line in open(train_file, 'r'):
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

    f = []
    for i in xrange(0, len(features)):
        f.append(0)

    for w in words:
        if w in features:
            ind = features.index(w)
            f[ind] += 1
        else:
            ind = unknown
            f[ind] += 1

    for i in xrange(0, len(features)):
        if f[i] == 0:
            pass
        else:
            s = "".join([" ", str(i+1), ":", str(f[i])])
            ans.append(s)
        
    return "".join(ans)

if __name__ == '__main__':
    features=makeFeatureList()

    for line in sys.stdin:
        l = line.rstrip("\n")
        print libsvmFormat(features, l)
