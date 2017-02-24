import numpy as np
import sys
import matplotlib.pyplot as plt
import warmUpExercise as we
import computeCost as cc
import plotData as pd
import pause as pause
import plotly.plotly as py

# ***************Pause()***************
def pause():
    programPause = input("Press the <ENTER> key to continue...")

# *************************************
print  ('Running warmUpExercise ... \n')
print ('5x5 Identity Matrix: \n')
we.warmUpExercise()
pause()

#*************plotting*****************
print ('Plotting Data ...\n')
array = np.loadtxt('ex1data1.txt',delimiter=',')
X = np.hsplit(array,2)
x = X[0]
y = X[1]
m = y.size
pd.plotData(x,y)

#***************GD****************
print ('Running Gradient Descent ...\n')
l = np.ones((m,1))
X = np.hstack((l,x))
theta = np.zeros((2,1))
iterations =1500
alpha = 0.01
cc.computeCost(X, y, theta)


def gradientDescent(X, y, theta, alpha, iterations):
    m = y.size
    add =0
    sub=0
    J_history = np.zeros((iterations,1))
    for iter in range(1,iterations):
        add=0
        sub=0
        i=1
        while (i <= m):
            add+= ((theta[0] * X[i - 1][0] + theta[1] * X[i - 1][1]) - y[i - 1])*(X[i - 1][1])
            sub+= (theta[0] * X[i - 1][0] + theta[1] * X[i - 1][1]) - y[i - 1]
            i+= 1
        theta[1]-=(alpha/m)*add
        theta[0]-=(alpha/m)*sub
        J_history[iter] = cc.computeCost(X, y, theta)




gradientDescent(X, y, theta, alpha, iterations)
print ('Theta found by gradient descent: ')
print (theta[0])
print (theta[1])
A = np.matrix('1 3.5')
B = np.matrix('1 7')
print ((A*theta)*10000)
print ((B*theta)*10000)