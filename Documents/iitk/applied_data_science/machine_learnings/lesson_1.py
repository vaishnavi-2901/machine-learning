import pandas as pd
import numpy as np

csv_file =r"C:\Users\vaish\Documents\iitk\applied_data_science\machine_learnings\preprocessExample.csv"
data  = pd.read_csv(csv_file)

# data = data.fillna()
# print(data)

# create a model that can predict if a customer can make a purchase on my site based on customer's age, salary and location

# Features: Country, Age, and Salary
# Label: Purchased? 
# 
# ML Model: Regression or Classification
# data label is categorical --> binary classification
# need inferential stats -->
# 1. data should be complete
# 2. data should be numeric

# package: scikit-learn

features = data.iloc[:, 0:3].values
label = data.iloc[:,[3]].values
# print(features)

# preprocessing starts
# handle missing valu
# step 1: import relevant package
from sklearn.impute import SimpleImputer
# step 2: Instantiate simpleimputer class
siForCountry = SimpleImputer(missing_values=np.nan, strategy="most_frequent")

# fit data to the object
# calculate the mode of the column 

siForCountry.fit(features[:,[0]])

# Transform the column --> fill value with the mode

features[:,[0]] = siForCountry.transform(features[:,[0]])


# do the same for age and salary columns
# to get the correct strategy, check outliers or skewness
# most frequent --> categorical data (gender, city, color)
# mean --> numeric and normally distributed data
# median --> numeric and skewed data

siForAge = SimpleImputer(fill_value=np.nan, strategy="median")
features[:,[1]] = siForAge.fit_transform(features[:,[1]])


# for salary
# siForSalary = SimpleImputer(strategy="mean")
# features[:,[2]] = siForSalary.fit_transform(features[:,[2]])
siForSalary = SimpleImputer(strategy="mean")
features[:,[2]] = siForSalary.fit_transform(features[:,[2]])


print(label)
from sklearn.preprocessing import OneHotEncoder

oheForCountry = OneHotEncoder(sparse_output=False)

countryOHE = oheForCountry.fit_transform(features[:,[0]])

# print(countryOHE)

# create final feature set
finalFeatureSet = np.concat((countryOHE, features[:,[1,2]]), axis=1) # based on columns
# print(finalFeatureSet)


# print(features)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=3)


# print(X_train)

# Initialise the algo --> LinearRegression

from sklearn.linear_model import LinearRegression

model = LinearRegression()

# starts the training
model.fit(X_train, y_train)

print(model.coef_) #b1
print(model.intercept_) #b0