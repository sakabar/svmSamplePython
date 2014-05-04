python src/outputFeatureList.py > featureList.txt
python src/outputLIBSVMformat.py < data/train_kakaku.txt > train_libsvmFormat.txt
python src/outputLIBSVMformat.py < data/test_kakaku.txt  >  test_libsvmFormat.txt
python src/main.py | tee result.txt
