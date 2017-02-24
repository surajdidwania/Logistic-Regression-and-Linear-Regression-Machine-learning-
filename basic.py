import numpy as np;
import csv;
import random
import matplotlib.pyplot as plt
# print(np.eye(5));
# A = np.matrix('1 2; 3 4')
# print (A)
# print (A.shape[0])
# size: no of elements in the array or matrix
# shape: dimenshions if the matrix
# B = np.matrix('1 2 3')
# print (B)
# print (2*np.ones((2,3)))
# print (np.zeros((2,2)))
# w = -6 +  np.sqrt(10)*(random.randint(1,10000))
# np.histogram(w)
# print (np.eye(3))
# reader = csv.reader(open("F:\Introduction to Algorithm\Project\CSV Format\routes.csv","rb"),delimeter)
# np.load("F:\\Introduction to Algorithm\\Project\\google_transit\\agency.txt")
A = np.matrix('1 2;3 4;5 6')
print (A.item((1,1)))
print (A[1,1])
print (A)
# A[1,:] = '11 12'
print (A[:])





