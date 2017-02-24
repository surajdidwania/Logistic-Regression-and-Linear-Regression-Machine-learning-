import matplotlib.pyplot as plt
from pylab import legend, where


def plotData1(X,Y):
    pos = where(Y == 1)
    neg = where(Y ==0)
    plt.scatter(X[pos,0],X[pos,1],marker = '+',color = 'r')
    plt.scatter(X[neg,0],X[neg,1],marker = 'o',color = 'b')
    plt.xlabel('Exam 1 score')
    plt.ylabel('Exam 2 score')
    legend(['Not Admitted', 'Admitted'])
    plt.show()