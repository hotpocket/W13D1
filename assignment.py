# this file is mostly similar to the ipynb but made for the terminal instead of the browser

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder

# load
df = pd.read_csv('employee_attrition.csv')
# pd.set_option('display.max_columns', 999) # don't hide column data

# show sample & data types
print(f'(rows, fields): {df.shape}\n')
print(df.head(n=3))
print({c:str(d) for c,d in zip(df.columns, df.dtypes)})

# the target variable is Attrition, the rest are feature variables.
target_variable = 'Attrition'
feature_variables = df.columns[df.columns != target_variable]
# print(f'\nTarget variable: {type(target_variable)}\n\t{target_variable}')
# print(f'\nFeature variables:  {type(feature_variables)}\n\t{list(feature_variables)}')

# what is a "missing value" ... zero?  null?  empty_string? ...
# print('\nNull Counts\n')
# sum the number of null values in each column
#display(pd.DataFrame([list(df.isnull().sum())], columns=df.columns, index=['']))

if df.isnull().sum().sum() == 0:
    print('No missing values')
else:
    print('Missing values found. Removing rows with missing values.')
    print(f'shape before drop: {df.shape}')
    df.dropna(inplace=True)
    print(f'shape after drop: {df.shape}')

# show the data types of each column
print('\nData Types\n')
#print(pd.DataFrame([list(df.dtypes)], columns=df.columns, index=['']))
print({c:str(d) for c,d in zip(df.columns, df.dtypes)})

# We categorize the features/fields into three categories (ordered, categoriecal, unrelated)
# we thus will use ordinal, label, one-hot, respectively
# This is a manual decision and will go like so


#{'Age': 'int64', 'Attrition': 'object', 'BusinessTravel': 'object', 'DailyRate': 'int64', 'Department': 'object', 'DistanceFromHome': 'int64', 'Education': 'int64', 'EducationField': 'object', 'EmployeeCount': 'int64', 'EmployeeNumber': 'int64', 'EnvironmentSatisfaction': 'int64', 'Gender': 'object', 'HourlyRate': 'int64', 'JobInvolvement': 'int64', 'JobLevel': 'int64', 'JobRole': 'object', 'JobSatisfaction': 'int64', 'MaritalStatus': 'object', 'MonthlyIncome': 'int64', 'MonthlyRate': 'int64', 'NumCompaniesWorked': 'int64', 'Over18': 'object', 'OverTime': 'object', 'PercentSalaryHike': 'int64', 'PerformanceRating': 'int64', 'RelationshipSatisfaction': 'int64', 'StandardHours': 'int64', 'StockOptionLevel': 'int64', 'TotalWorkingYears': 'int64', 'TrainingTimesLastYear': 'int64', 'WorkLifeBalance': 'int64', 'YearsAtCompany': 'int64', 'YearsInCurrentRole': 'int64', 'YearsSinceLastPromotion': 'int64', 'YearsWithCurrManager': 'int64'}