# -*- coding: utf-8 -*-
"""day27-one-hot-encoding.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nKlUHrDm6h_vXF29MfO-DShVTULgD6Vq
"""

import numpy as np
import pandas as pd

df = pd.read_csv('/content/cars.csv')

df.head()

df['owner'].value_counts()

"""**1. OneHotEncoding using Pandas**"""

pd.get_dummies(df,columns=['fuel','owner'])

"""**2. K-1 OneHotEncoding**"""

pd.get_dummies(df,columns=['fuel','owner'],drop_first=True)

"""**3. OneHotEncoding using Sklearn**"""

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(df.iloc[:,0:4],df.iloc[:,-1],test_size=0.2,random_state=2)

X_train.head()

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(drop='first', sparse_output=False, dtype=np.int32)

X_train_new = ohe.fit_transform(X_train[['fuel','owner']])

X_test_new = ohe.transform(X_test[['fuel','owner']])

X_train_new.shape

np.hstack((X_train[['brand','km_driven']].values,X_train_new))

"""**4. OneHotEncoding with Top Categories**"""

counts = df['brand'].value_counts()

df['brand'].nunique()
threshold = 100

repl = counts[counts <= threshold].index

pd.get_dummies(df['brand'].replace(repl, 'uncommon')).sample(5)