'''
Created on 24 Sept 2024
Name     : Sunder Rajan
Type     : Forex Hedged USD
Server   : MetaQuotes-Demo
Login    : 86791898
Password : 4+OwMhRv
Investor : WaV+Z4Bo

@author: sunde
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from master_function import data_preprocessing,mass_import
from master_function import plot_train_test_values
from master_function import calculate_accuracy,model_bias, RMSE
from master_function import connect, excel_import
from sklearn.metrics import mean_squared_error

from xgboost import XGBRegressor

USE_EXCEL= False
FILENAME = "C://Users/sunde/Documents/Python Scripts/historical_data.xlsx" 

#auth = connect()
if USE_EXCEL:
    data = np.diff(excel_import(FILENAME).iloc[:,4])
else:    
    data = np.diff(mass_import(0,'H1')[:,3]) # get the closing values of OHLC i.e. 3rd column

num_lags = 500  # number of lagged values we use for prediction
train_test_split = 0.80

x_train,y_train,x_test, y_test = data_preprocessing(data,num_lags, train_test_split)

# now fit the model
model = XGBRegressor(random_state=123, n_estimators=16, max_depth=12)
model.fit(x_train,y_train)    
    
y_predicted_train = np.reshape(model.predict(x_train),(-1,1))
y_predicted       = np.reshape(model.predict(x_test),(-1,1))

plot_train_test_values(100,50,y_train,y_test,y_predicted)

acc_train = calculate_accuracy(y_predicted_train, y_train)
acc_test  = calculate_accuracy(y_predicted, y_test)
print("Train accuracy: " +str(acc_train) + ", Test accuracey: " + str(acc_test))

mb_train = model_bias(y_predicted_train)
mb_test = model_bias(y_predicted)
print("Bias train: " + str(mb_train) +", test bias: " + str(mb_test))

print("RSME test:" + str(RMSE(y_predicted,np.reshape(y_test,(-1,1)))))
print("RSME train:" + str(RMSE(y_predicted_train,np.reshape(y_train,(-1,1)))))

# correlation
test_corr = pd.DataFrame({'col1': y_predicted[:,0], 'col2': y_test}).corr()
print("Test correlation " + str(test_corr))

train_corr = pd.DataFrame({'col1': y_predicted_train[:,0], 'col2': y_train}).corr()
print("Train correlation " + str(train_corr))     

