# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 22:14:13 2020

@author: MAHENDER
"""

from sklearn import preprocessing
import numpy as np
# Get dataset
df = pd.read_csv("E:\prediction\prd\pm.csv", sep=",")
# Normalize total_bedrooms column
x_array = np.array(df['PRODUCTION'])
normalized_X = preprocessing.normalize([x_array])




from sklearn import preprocessing
# Get column names first
names = df.columns
# Create the Scaler object
scaler = preprocessing.StandardScaler()
# Fit your data on the scaler object
scaled_df = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_df, columns=names)


# Create range for your new columns
lat_range = zip(xrange(32, 44), xrange(33, 45))
new_df = pd.DataFrame()
# Iterate and create new columns, with the 0 and 1 encoding
for r in lat_range:
        new_df["latitude_%d_to_%d" % r] = df["latitude"].apply(
            lambda l: 1.0 if l >= r[0] and l < r[1] else 0.0)
new_df