#coding: utf-8
import liblinearutil
import outputLIBSVMformat

train_label, train_data = liblinearutil.svm_read_problem("./train_libsvmFormat.txt")
#カーネル関数は線型
model = liblinearutil.train(train_label, train_data, "-s 3")

test_label, test_data = liblinearutil.svm_read_problem("./test_libsvmFormat.txt")
p_label, p_acc, p_val = liblinearutil.predict(test_label, test_data, model)

