# -*- coding: utf-8 -*-
"""missing-category-imputation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_JOkK1qCWpdsTTDDaoCSmDWo-64kRXLj
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/content/train.csv',usecols=['GarageQual','FireplaceQu','SalePrice'])

df.head()

df.isnull().mean()*100

df['GarageQual'].value_counts().sort_values(ascending=False).plot.bar()
plt.xlabel('GarageQual')
plt.ylabel('Number of houses')

df['GarageQual'].fillna('Missing', inplace=True)

df['GarageQual'].value_counts().sort_values(ascending=False).plot.bar()
plt.xlabel('GarageQual')
plt.ylabel('Number of houses')

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(df.drop(columns=['SalePrice']),df['SalePrice'],test_size=0.2)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='constant',fill_value='Missing')

X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_train)

imputer.statistics_