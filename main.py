
import pandas as pd
from numpy.ma.core import zeros

#load the datasets(keep these at the very top)
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")
#=====
#TASK 1:Check shapes and target column
print("Train shape:",train.shape)
print("Test shape:",test.shape)
target_col=[col for col in train.columns if col not in test.columns]
print("our target column is:",target_col)
#=====
#TASK 2:check for missing values
#======
missing_counts=train.isnull().sum()
missing_columns=missing_counts[missing_counts>0]
print(missing_columns)
#====
#Task 3:visualize missing data with a pie chart
#====
import matplotlib.pyplot as plt
#create a bar plot of the missing columns
missing_columns.plot(kind='bar',figsize=(10,15))
plt.title("missing values count per column")
plt.ylabel("number of missing values")
plt.xlabel("columns")
plt.tight_layout()
#show the window with the graph
plt.show()
#===
# task 4:  clean missing values(imputation)
#====
train['GarageYrBlt']=train['GarageYrBlt'].fillna(0)
train['MasVnrArea']=train['MasVnrArea'].fillna(0)
#let's check if they are fixed
remaining_missing=train[['GarageYrBlt','MasVnrArea']].isnull().sum()
print("missing values left in cleaned columns:")
print(remaining_missing)
#=======
#task 5:clean columns & rare checks
#=====
#fix alley:fill missing text with "none"
train['Alley']=train['Alley'].fillna("none")
#fix electrical:fill the single missing value with the most common value (mode)
most_common_electrical=train['Electrical'].mode()[0]
train['Electrical']=train['Electrical'].fillna(most_common_electrical)
#let's check our work on these columns!
text_cleaning_check=train[['Alley','Electrical']].isnull().sum()
print("\nMissing values left in text column:")
print(text_cleaning_check)
#=========
#task 6:bulk clean all remaining columns
#==========
#1.find any remaining columns that still have missing values
remaining_cols=train.columns[train.isnull().sum()>0]
#2.loop through them:fill text with "none" and numbers with 0
for col in remaining_cols:
    if train[col].dtype=='object':
        train[col]=train[col].fillna("none")
    else:
        train[col]=train[col].fillna(0)
#FINAL VERIFICATION:check total missing values in the entire dataset
print("\nTotal missing values left in the dataset;",train.isnull().sum())
