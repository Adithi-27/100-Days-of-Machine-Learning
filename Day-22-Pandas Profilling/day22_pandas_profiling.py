# -*- coding: utf-8 -*-
"""day22-pandas-profiling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n1wl0_NOpJ5XFLEI_2w9bn5S8rXB9e3j
"""

import pandas as pd

df = pd.read_csv('/content/train.csv')

df.head()

!pip install pydantic-settings
!pip install -U pandas-profiling[notebook,html] --no-cache-dir
!pip install ydata-profiling

from ydata_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='output.html')