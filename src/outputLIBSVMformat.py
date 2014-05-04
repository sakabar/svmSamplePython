#coding: utf-8
import sys
#import svmutil

def load():
    #素性番号1は"未定義語"
    features=["未定義"]

    for line in open('./data/train_kakaku.txt', 'r'):
        for w in line.split(" ")[1:]:
            if w in features:
                pass
            else:
                features.append(w)
        
    return features

# featureリストと一行のラベル, 単語列を引数として、文字列を返す
def libsvmFormat(features, line):
    lst = line.split(" ")
    label = lst[0]
    words = lst[1:]
    ans = [label]

    f = []
    for i in xrange(0, len(features)):
        f.append(0)

    for w in words:
        ind = features.index(w)
        f[ind] += 1
    
    for i in xrange(0, len(features)):
        s = "".join([" ", str(i+1), ":", str(f[i])])
        ans.append(s)

    return "".join(ans)

if __name__ == '__main__':
    features=load()
        
    for line in open('./data/train_kakaku.txt', 'r'):
        print libsvmFormat(features, line)

        
