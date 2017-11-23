#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Import Library
# Import other necessary libraries like pandas, numpy...
import numpy
from sklearn import linear_model

# Load Train and Test datasets
# Identify feature and response variable(s) and values must be numeric and numpy arrays
x_train = numpy.reshape([1,2,3,4,5,6,7,8],[8,1]) #input_variables_values_training_datasets
y_train = numpy.reshape([0.52,9.36,53,191,350.18,571.12,912.17,1207],[8,1]) #target_variables_values_training_datasets
x_test = [[9],[1680]] #input_variables_values_test_datasets

# Create linear regression object
linear = linear_model.LinearRegression()

# Train the model using the training sets and check score
linear.fit(x_train, y_train)
linear.score(x_train, y_train)

# Equation coefficient and Intercept
print('Coefficient: ', linear.coef_)
print('Intercept: ', linear.intercept_)

# Predict Output
predicted = linear.predict(x_test)
print predicted