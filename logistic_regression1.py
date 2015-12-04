__author__ = 'lenovo-pc'

import numpy as np

N = 100
D = 2
X = np.random.randn(N,D)
w= np.random.randn(D+1,1)
ones = np.array([[1]*N]).T
Xb = np.concatenate((ones,X), axis=1)
z = Xb.dot(w)

def sigmoid(x) :
    return(1/1+np.exp(-x))

print (sigmoid(z))
