import numpy as np
import plotData1 as pd
import sigmoid as sm
import costFunction as cf
print ('Plotting Data ...\n')
data = np.loadtxt('ex2data1.txt',delimiter=',')
X = data[:, 0:2]
y = data[:, 2]
pd.plotData1(X,y)
####=========== Part 2: Compute Cost and Gradient ============
m,n = X.shape
n = 2
l  = np.ones((m,1))
X = np.hstack((l,X))
initial_theta = np.zeros((1,n+1))

cost = cf.cost(initial_theta,X,y)
grad = cf.gradient(initial_theta,X,y)
print (cost)
print  (grad)
