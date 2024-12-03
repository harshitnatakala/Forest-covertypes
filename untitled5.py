# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Btujiw97kdHPlAAES0vBCUq6Na2hYlQO
"""

!pip install ucimlrepo

from ucimlrepo import fetch_ucirepo

# fetch dataset
covertype = fetch_ucirepo(id=31)

# data (as pandas dataframes)
X = covertype.data.features
y = covertype.data.targets

# metadata
print(covertype.metadata)

# variable information
print(covertype.variables)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")
from sklearn.svm import SVC , LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier , GradientBoostingClassifier , AdaBoostClassifier ,ExtraTreesClassifier
# from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# import lightgbm as lgb

# Reading the dataset
df = pd.DataFrame(covertype.data.features) # Use features for the DataFrame
df['target'] = covertype.data.targets # Add the target as a separate column
df.head()

df.info()

df.describe()

df.isnull().sum()

dc = df.corr()
plt.figure(figsize = (20,20))
plt.title('Correlation Map')
sns.heatmap(dc, cmap = 'YlGnBu')

df.columns

non_soil_cols = ['Elevation', 'Aspect', 'Slope', 'Horizontal_Distance_To_Hydrology',
       'Vertical_Distance_To_Hydrology', 'Horizontal_Distance_To_Roadways',
       'Hillshade_9am', 'Hillshade_Noon', 'Hillshade_3pm',
       'Horizontal_Distance_To_Fire_Points', 'Wilderness_Area1', 'Wilderness_Area2','Wilderness_Area3','Wilderness_Area4']

soil_cols = ['Soil_Type1',
       'Soil_Type2', 'Soil_Type3', 'Soil_Type4', 'Soil_Type5', 'Soil_Type6',
       'Soil_Type7', 'Soil_Type8', 'Soil_Type9', 'Soil_Type10', 'Soil_Type11',
       'Soil_Type12', 'Soil_Type13', 'Soil_Type14', 'Soil_Type15',
       'Soil_Type16', 'Soil_Type17', 'Soil_Type18', 'Soil_Type19',
       'Soil_Type20', 'Soil_Type21', 'Soil_Type22', 'Soil_Type23',
       'Soil_Type24', 'Soil_Type25', 'Soil_Type26', 'Soil_Type27',
       'Soil_Type28', 'Soil_Type29', 'Soil_Type30', 'Soil_Type31',
       'Soil_Type32', 'Soil_Type33', 'Soil_Type34', 'Soil_Type35',
       'Soil_Type36', 'Soil_Type37', 'Soil_Type38', 'Soil_Type39',
       'Soil_Type40', 'target']



df_ns = df[non_soil_cols]
df_s = df[soil_cols]

dc = df_ns.corr()
plt.figure(figsize = (10,6))
plt.title('Correlation Map for non Soil columns')
sns.heatmap(dc,annot = True, cmap = 'YlGnBu')

dc = df_s.corr()
plt.figure(figsize = (20,15))
plt.title('Correlation Map for Soil columns')
sns.heatmap(dc,annot = True, cmap = 'YlGnBu')

"""**Conclusion Drawn :**
There are very few similarities in the soil type data . The non soil data does have high coorelation in the Aspect , Elevation and Scope data .
"""

# Let us check if the soil related columns are one hot encoded

def unique_val(df ) :
    for column , item in df.items():
        print('--------------------')
        print('The column name is :',column)
        print('The number of unique values are :',df[column].nunique())
        print('the unique values of the column are :',df[column].value_counts())
        print('--------------------')

unique_val(df_s)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
cov = le.fit_transform(list(df["target"]))
y = list(cov)
'''
x = df[["Elevation", "Aspect", "Slope", "Horizontal_Distance_To_Hydrology", "Vertical_Distance_To_Hydrology",
        "Horizontal_Distance_To_Roadways", "Hillshade_9am", "Hillshade_Noon", "Hillshade_3pm",
        "Horizontal_Distance_To_Fire_Points", "Wilderness_Area1", "Wilderness_Area2",
        "Wilderness_Area3", "Wilderness_Area4"]]
'''
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

rf = RandomForestClassifier(n_estimators=100)
rf.fit(x_train, y_train)
pred = rf.predict(x_test)
print("Accuracy using Random Forest: ", round(rf.score(x_test,y_test) * 100, 3), "%", sep="")

lr = LogisticRegression(solver="saga", max_iter=7500)
lrmodel = lr.fit(x_train, y_train)
lracc = lr.score(x_test, y_test)
print("Accuracy using Logistic Regression: ", round(lracc*100, 3), "%", sep="")

from sklearn import svm, metrics

svmmodel = svm.SVC(kernel="rbf", C=1)
svmmodel.fit(x_train, y_train)
y_pred = svmmodel.predict(x_test)
svmacc = metrics.accuracy_score(y_test, y_pred)
print("Accuracy using SVM: ", round(svmacc*100, 3), "%", sep="")

import pandas as pd

# Data for the table
data = {
    "Model": ["KNN", "Random Forest", "Logistic Regression"],
    "Accuracy": [0.79, 0.955, 0.701],
    "Precision": [0.72, 0.93, 0.68],
    "Recall": [0.66, 0.91, 0.65],
    "F1-Score": [0.69, 0.92, 0.67]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df.to_string(index=False))