# predict the profit of the company based on company's spending pattern and location


import pandas as pd
import numpy as np


csv_file = r"C:\Users\vaish\Documents\iitk\applied_data_science\machine_learnings\50_Startups.csv"
data = pd.read_csv(csv_file)

# print(data.info())

# ṣeparate data as feature and model

label = data.iloc[:,[4]].values

features = data.iloc[:,[0,1,2,3]].values

# print(features, label)

# since the column state is categorical use OHE

from sklearn.preprocessing import OneHotEncoder

OheForState = OneHotEncoder(sparse_output=False)

stateOhe = OheForState.fit_transform(features[:,[3]])

# print(stateOhe)

finalfeatureSet = np.concat((stateOhe, features[:,[0,1,2]]), axis=1) #column based

# print(finalfeatureSet)

# override features set for better readibility

fetaures = finalfeatureSet
# print(fetaures)

SL = 0.1
CL = 1-SL

# split the training and testing data
# lable = profit
# label type = continous ND
# algorith = Regression

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(finalfeatureSet, label, test_size=0.2, random_state=10)


# print(X_train, y_train)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)


testscore = model.score(X_test, y_test)
trainscore = model.score(X_train, y_train)

print(testscore, trainscore)

# print(model.coef_) #b1
# print(model.intercept_) #b0

rdSpend = float(input("Enter RD Spend: "))
adminSpend = float(input("Enter Admin Spend: "))
markSpend = float(input("Enter Marketing Spend: "))
state = input("Enter State: ")


if state in OheForState.categories_[0]:
    dummyState = OheForState.transform(np.array([[state]]))

    finalFeatureInput = np.concat((dummyState, np.array([[rdSpend, adminSpend, markSpend]])), axis=1)

    profit = model.predict(finalFeatureInput)

    print(f"Predicted profit is: ${profit}")


else:
    print(f"{state} is not recognised by AI model!")


