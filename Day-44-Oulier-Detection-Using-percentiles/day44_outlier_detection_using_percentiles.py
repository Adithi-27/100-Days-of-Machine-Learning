# -*- coding: utf-8 -*-
"""day44-outlier-detection-using-percentiles.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11280diR1apuM1LBkwdw-5jE3MJSj2els
"""

import numpy as np
import pandas as pd

df = pd.read_csv('/content/weight-height.csv')

df.head()

df.shape

df['Height'].describe()

import seaborn as sns

sns.distplot(df['Height'])

sns.boxplot(df['Height'])

upper_limit = df['Height'].quantile(0.99)
upper_limit

lower_limit = df['Height'].quantile(0.01)
lower_limit

new_df = df[(df['Height'] <= 74.78) & (df['Height'] >= 58.13)]

new_df['Height'].describe()

df['Height'].describe()

sns.distplot(new_df['Height'])

sns.boxplot(new_df['Height'])

# Capping --> Winsorization
df['Height'] = np.where(df['Height'] >= upper_limit,
        upper_limit,
        np.where(df['Height'] <= lower_limit,
        lower_limit,
        df['Height']))

df.shape

df['Height'].describe()

sns.distplot(df['Height'])

sns.boxplot(df['Height'])