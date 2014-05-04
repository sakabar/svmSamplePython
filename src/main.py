import sys
import svmutil

train_label, train_data = svmutil.svm_read_problem("./train_libsvmFormat.txt")
model = svmutil.svm_train(train_label, train_data)

test_label, test_data = svmutil.svm_read_problem("./train_libsvmFormat.txt")
p_label, p_acc, p_val = svmutil.svm_predict(test_label, test_data, model)

