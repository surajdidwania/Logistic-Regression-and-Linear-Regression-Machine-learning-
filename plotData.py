import numpy as np
import sys
import matplotlib.pyplot as plt

def plotData(X,Y):
    plt.scatter(X,Y)
    plt.xlabel('Population of City in 10,000s',fontsize =12)
    plt.ylabel('Profit in $10,000s',fontsize =12)
    plt.show()
