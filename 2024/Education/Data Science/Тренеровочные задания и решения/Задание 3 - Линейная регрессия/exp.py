import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, mean_absolute_error 
from sklearn import preprocessing 
  
# importing data 
df = pd.read_csv('Real-estate1.csv') 
df.drop('No', inplace=True, axis=1) 
  
print(df.head()) 
  
print(df.columns) 
  
# plotting a scatterplot 
sns.scatterplot(x='X4 number of convenience stores', 
                y='Y house price of unit area', data=df) 
  
# creating feature variables 
X = df.drop('Y house price of unit area', axis=1) 
y = df['Y house price of unit area'] 
  
print(X) 
print(y) 
  
# creating train and test sets 
X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size=0.3, random_state=101) 
  
# creating a regression model 
model = LinearRegression() 
  
# fitting the model 
model.fit(X_train, y_train) 
  
# making predictions 
predictions = model.predict(X_test) 
  
# model evaluation 
print('mean_squared_error : ', mean_squared_error(y_test, predictions)) 
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions)) 