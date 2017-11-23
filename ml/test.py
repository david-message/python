# coding:utf-8

import numpy as np
import random
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

arr = np.linspace(0,25,26)
arr1 = np.reshape(arr,[len(arr),1])

print arr,'\n',arr1