# -*- coding: utf-8 -*-
"""
Created on Mon May 24 12:37:09 2021

@author: alize
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import glob
all_data=pd.DataFrame()
for f in glob.glob(r"C:\Users\alize\Desktop\weather\*.csv"):
    df=pd.read_csv(f,sep=",")
all_data=all_data.append(df,ignore_index=True)
print(df)
print(all_data)
df.info()
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
plt.hist(df.Temperature,bins=12,color='#9acd32',
         histtype="step",label="Temperature/30")
plt.xlabel("Months")
plt.ylabel("Average Temperature")

january=pd.read_csv(r"C:\Users\alize\Desktop\weather\ocak2020.csv")
print(january)

february=pd.read_csv(r"C:\Users\alize\Desktop\weather\şubat2020.csv")
print(february)

march=pd.read_csv(r"C:\Users\alize\Desktop\weather\mart2020.csv")
print(march)

april=pd.read_csv(r"C:\Users\alize\Desktop\weather\nisan2020.csv")
print(april)

may=pd.read_csv(r"C:\Users\alize\Desktop\weather\mayıs2020.csv")
print(may)

june=pd.read_csv(r"C:\Users\alize\Desktop\weather\haziran2020.csv")
print(june)

july=pd.read_csv(r"C:\Users\alize\Desktop\weather\temmuz2020.csv")
print(july)

august=pd.read_csv(r"C:\Users\alize\Desktop\weather\ağustos2020.csv")
print(august)


sept=pd.read_csv(r"C:\Users\alize\Desktop\weather\eylül2020.csv")
print(sept)

octt=pd.read_csv(r"C:\Users\alize\Desktop\weather\ekim2020.csv")
print(octt)

nov=pd.read_csv(r"C:\Users\alize\Desktop\weather\kasım2020.csv")
print(nov)
dec=pd.read_csv(r"C:\Users\alize\Desktop\weather\aralık2020.csv")
print(dec)



