#!/usr/bin/python

import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score
from time import time

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.neighbors import KNeighborsClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]

#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")


# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# k nearest neighbors
def k_nearest():
    n_neighbors = 1
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    t0 = time()
    clf.fit(features_train, labels_train)
    print "k Nearest training time:", round(time() - t0, 3), "s"
    t0 = time()
    predict = clf.predict(features_test)
    print "k Nearest training time:", round(time() - t0, 3), "s"

    accuracy = accuracy_score(predict, labels_test)
    print "K Nearest Accuracy with {} Neighbors is: {}".format(n_neighbors, accuracy)
    return clf


def random_forest():
    max_depth = 50
    min_sample_split = 125
    clf = RandomForestClassifier(max_depth=max_depth, min_samples_split=min_sample_split)
    t0 = time()
    clf.fit(features_train, labels_train)
    print "Random Forest training time:", round(time() - t0, 3), "s"
    t0 = time()
    predict = clf.predict(features_test)
    print "Random Forest training time:", round(time() - t0, 3), "s"

    accuracy = accuracy_score(predict, labels_test)
    print "Random Forest Accuracy with {} Max Depth & {} Min Sample Split is: {}".format(
        max_depth, min_sample_split, accuracy)
    return clf


def ada_boost():
    clf = AdaBoostClassifier(n_estimators=25)
    t0 = time()
    clf.fit(features_train, labels_train)
    print "Ada Boost training time:", round(time() - t0, 3), "s"
    t0 = time()
    predict = clf.predict(features_test)
    print "Ada Boost training time:", round(time() - t0, 3), "s"

    accuracy = accuracy_score(predict, labels_test)
    print "Ada Boost Accuracy: {}".format(accuracy)
    return clf


clf = k_nearest()
clf = random_forest()
clf = ada_boost()

try:
    plt = prettyPicture(clf, features_test, labels_test)
    plt.show()
except NameError as e:
    pass
