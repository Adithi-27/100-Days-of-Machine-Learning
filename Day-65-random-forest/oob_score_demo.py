# -*- coding: utf-8 -*-
"""oob-score-demo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17n_N-iLQIGD_fg2wvWhwolYSH2k3onNc
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

df = pd.read_csv('heart.csv')
df.head()

X = df.iloc[:,0:-1]
y = df.iloc[:,-1]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

rf = RandomForestClassifier(oob_score=True)

rf.fit(X_train,y_train)

rf.oob_score_

y_pred = rf.predict(X_test)
accuracy_score(y_test,y_pred)