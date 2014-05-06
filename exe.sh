python src/outputFeatureList.py > featureList.txt
python src/outputLIBSVMformat.py < data/train_kakaku.txt > train_libsvmFormat.txt
python src/outputLIBSVMformat.py < data/test_kakaku.txt  >  test_libsvmFormat.txt
python src/main_libsvm.py | tee result_libsvm.txt
echo ""
python src/main_liblinear.py | tee result_liblinear.txt
