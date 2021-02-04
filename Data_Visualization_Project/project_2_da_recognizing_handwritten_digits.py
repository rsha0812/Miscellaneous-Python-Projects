# -*- coding: utf-8 -*-
"""Project 2_DA_Recognizing Handwritten Digits.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I2Oqu55yVzolhpN6Pa32U0JRlBLA5TvX
"""

from sklearn import svm
svc = svm.SVC(gamma=0.001, C=100.)

"""#Loading DataSet"""

from sklearn import datasets
digits = datasets.load_digits()

#Desciption of 8x8 data set 
print(digits.DESCR)

digits.images[9] # Array representation of digit 9

"""#Graphical Representation of Digit """

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
plt.imshow(digits.images[9], cmap=plt.cm.gray_r, interpolation='nearest')

digits.target # DataSize 
digits.target.size

"""#Learning and Predicting Model

#First Case
"""

# Commented out IPython magic to ensure Python compatibility.
#Taken set of first six images of total 1797 elements as validation set
# 1791 elements are taken as training set to train the data 
import matplotlib.pyplot as plt
# %matplotlib inline
plt.subplot(321)
plt.imshow(digits.images[1], cmap=plt.cm.gray_r,
interpolation='nearest')
plt.subplot(322)
plt.imshow(digits.images[2], cmap=plt.cm.gray_r,
interpolation='nearest')
plt.subplot(323)
plt.imshow(digits.images[3], cmap=plt.cm.gray_r,
interpolation='nearest')
plt.subplot(324)
plt.imshow(digits.images[4], cmap=plt.cm.gray_r,
interpolation='nearest')
plt.subplot(325)
plt.imshow(digits.images[5], cmap=plt.cm.gray_r,
interpolation='nearest')
plt.subplot(326)
plt.imshow(digits.images[6], cmap=plt.cm.gray_r,
interpolation='nearest')

svc.fit(digits.data[7:1797], digits.target[7:1797])

svc.predict(digits.data[1:6])

digits.target[1:6]

"""#Second Case """

svc.predict(digits.data[20:27])

digits.target[20:27]

"""#Third Case"""

svc.predict(digits.data[1020:1025])

digits.target[1020:1025]