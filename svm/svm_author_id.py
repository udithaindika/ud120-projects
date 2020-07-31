#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

from sklearn.metrics import accuracy_score

sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

# c_values = [10.0, 100., 1000., 10000.]
# features_train = features_train[:len(features_train) / 100]
# labels_train = labels_train[:len(labels_train) / 100]

c_values = [10000.]

for c_value in c_values:
    clf = svm.SVC(kernel="rbf", C=c_value)
    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time() - t0, 3), "s"

    t0 = time()
    prediction = clf.predict(features_test)
    print "predict time:", round(time() - t0, 3), "s"

    accuracy = accuracy_score(prediction, labels_test)
    print "With C: {} Accuracy : {}".format(c_value, accuracy)

    cris_total = 0
    for i in prediction:
        if int(i) == 1:
            cris_total += 1

    print "Total Cris Emails :", cris_total

#########################################################
