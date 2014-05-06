#coding: utf-8
import sys
import svmutil
import outputLIBSVMformat

train_label, train_data = svmutil.svm_read_problem("./train_libsvmFormat.txt")
#カーネル関数は線型
model = svmutil.svm_train(train_label, train_data, "-t 0")

test_label, test_data = svmutil.svm_read_problem("./test_libsvmFormat.txt")
p_label, p_acc, p_val = svmutil.svm_predict(test_label, test_data, model)

