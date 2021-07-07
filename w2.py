# -*- coding: utf-8 -*-
"""
Created on Sat May 15 04:00:13 2021

@author: alize
"""
import glob
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

path =r"C:\Users\alize\Desktop\weather"
file_identifier = "*.csv"

all_data = pd.DataFrame()
for f in glob.glob(path + "/*" + file_identifier):
    df = pd.read_csv(f)
    all_data = all_data.append(df,ignore_index=True)
    print(all_data)
    all_data.to_csv("2020.csv")
    plt.hist(all_data.Conditions,bins=12,color='#9acd32',
         histtype="step",label="Temperature/30")
plt.xlabel("Conditions")
plt.ylabel("Average Temperatures")

X = all_data.iloc[:, 0].values.reshape(-1, 1) # values converts it into a numpy array
Y = all_data.iloc[:, 1].values.reshape(-1, 1) # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)