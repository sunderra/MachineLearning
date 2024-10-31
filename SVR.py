'''
Created on 25 Sept 2024

SUPPORT VECTOR MACHINES SVM
@author: sunde
'''
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.svm import SVR 
  
# generate synthetic data 
X = np.sort(5 * np.random.rand(40, 1),axis=0) 
y = np.sin(X).ravel() 
  
# add some noise to the data - change every 5th element
y[::5] += 3 * (0.5 - np.random.rand(8)) 
  
# create an SVR model with a linear kernel 
#svr = SVR(kernel='linear') 
#svr = SVR(kernel='poly')
svr = SVR(kernel='rbf')
  
# train the model on the data 
svr.fit(X, y) 
  
# make predictions on the data 
y_pred = svr.predict(X) 
  
# plot the predicted values against the true values 
plt.scatter(X, y, color='darkorange', 
            label='data') 
plt.plot(X, y_pred, color='cornflowerblue', 
         label='prediction') 
plt.legend() 
plt.show() 