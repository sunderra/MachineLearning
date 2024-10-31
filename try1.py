'''
Created on 23 Sept 2024

@author: sunde
'''
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

