'''
Created on 23 Sept 2024

@author: sunde
'''
from random import random

import pandas as pd
import numpy as np

data = {'col1':[1,2,3],'col2':[5,6,7]}

my_frame= pd.DataFrame(data)
my_array = np.array([[1,4],[2,3],[5,6]])

print(my_frame)
print(my_array)

first_array = np.array([1,2,3,5,8,13])
second_array= np.array([21,34,55,89,144,233])

# this reshape make a single column with unknown rows i.e. -1
first_array = np.reshape(first_array,(-1,1))
second_array = np.reshape(second_array,(-1,1))

combined_array = np.concatenate((first_array, second_array), axis=1)
#print(combined_array)

first_frame = pd.DataFrame({'col1': [1,2,3], 'col2': [4,5,6]})
second_frame = pd.DataFrame({'col1': [11,12,13], 'col2': [14,15,16]})
combined_frame = pd.concat([first_frame, second_frame], axis=1)
#print(combined_frame)

# referencing data frame items
my_df = pd.DataFrame({'col1' : [1,2,3,4,5,6,7,8,9,10]})
#print(my_df.iloc[-3:]['col1'])

my_df = pd.DataFrame({
                       'col1': [1,6,11],
                       'col2': [2,7,12],
                       'col3': [3,8,13],
                       'col4': [4,9,14],
                       'col5': [5,10,15] 
                    })

#print(my_df.iloc[-1:,])

# read excel file
FILENAME = "historical_data.xlsx"
data= pd.read_excel(FILENAME)
print(data["<CLOSE>"])

# HOW TO USE FORMAT COMMANDS
products = ['Product 1', 'Product 2']
times    = (1,3,6,12)   # this is a tuple
prices   = (500.1234,1000.46757)

print("Price of {} is for {} months is ${:.2f}".format(products[1], times[2], prices[1]) )

for i in times:
    print(i, end=",")

# list comprehensions
numbers = list(range(1,100,5))

new_numbers = [n * 2 for n in numbers]

new_list_comp = [i + j for i in range(2) for j in range(5)]

new_list_comp1 = [num**3 for num in range(1,11) if num %2 != 0 ]

new_list_comp2 = [num**3 if num %2 !=0 else "even" for num in range(1,11)]

# LAMBDA FUNCTIONS - ANONYMOUS FUNCTIONS

(lambda x: x**2) (11)

(lambda x,y: x + y) (3,5)

# here 2nd parameter is a function
sum_xy = lambda x,y: x + y(x)
sum_xy(2, lambda x: x**2)

# PANDAS INTRO

product_series = pd.Series(products)

daily_rates = pd.Series([10,20,30,40,50])

# NUMPY to PANDAS
np_array = np.array(range(10,100,10))

series_a = pd.Series(np_array)

data = pd.read_csv("agesonly.csv", header=None)
data_f= data.copy() # a deep copy so that the original data is not changed if we change this

data_f.describe()

data_f.nunique()   # numer of unique values

numbers =  pd.Series([15, 1000,23, 5,56])

# PANDAS DATAFRAMES

array_a = np.array([[3,2,1],[10,12,56]])
df = pd.DataFrame(array_a, index= ['Row 1', 'Row 2'], columns=['Col1','Col 2','Col 3'])


data = pd.read_excel("historical_data.xlsx", index_col=0)
data_f= data.copy() # a deep copy so that the original data i

data_f.index # provides the index column values i.e Dates
data_f.columns # provides column names
data_f.axes  # row and column info together
data_f.dtypes  #types of columnar data
data_f.values # an array of row by row of lists of columns

data_f.to_numpy()
data_f.shape    # provides row and column dimensions



