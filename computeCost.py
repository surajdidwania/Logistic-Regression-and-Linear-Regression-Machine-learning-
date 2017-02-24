import numpy as np
def computeCost(X, y, theta):
    m = y.size
    J=0
    i = 1
    while(i<=m):
        J+= np.square((theta[0]*X[i-1][0]+theta[1]*X[i-1][1])-y[i-1])
        i+=1
    J/=(2*m)
    # print (J)
