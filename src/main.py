#coding: utf-8
import svmutil

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

# "-1 hoge bar baz"を引数として、
#def change(features):
    

if __name__ == '__main__':
    features=load()
    
    #for line in open('./data/train_kakaku.txt', 'r'):
