import sys
import outputLIBSVMformat

if __name__ == '__main__':
    features=outputLIBSVMformat.makeFeatureList()
        
    for i in xrange(0, len(features)):
        print " ".join([str(i+1), features[i]])
