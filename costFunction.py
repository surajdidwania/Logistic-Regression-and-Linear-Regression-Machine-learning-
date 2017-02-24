import math
import numpy as np
import sigmoid as sg
def cost(initial_theta,x,y):
    theta = np.matrix(initial_theta)
    X = np.matrix(x)
    Y = np.matrix(y)
    n = Y.size
    first = np.multiply(-Y,np.log(sg.sigmoid(X*theta.T)))
    second = np.multiply(1-Y,np.log(1-sg.sigmoid(X*theta.T)))
    return np.sum(first-second)/len(X)

def gradient(initial_theta,x,y):
    theta = np.matrix(initial_theta)
    X = np.matrix(x)
    Y = np.matrix(y)
    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)
    error = sg.sigmoid(X * theta.T) - y
    for i in range(parameters):
        term = np.multiply(error, X[:, i])
        grad[i] = np.sum(term) / len(X)
    return grad