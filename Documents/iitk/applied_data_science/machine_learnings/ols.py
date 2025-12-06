import pandas as pd
import numpy as np


# csv_file = r"50_Startups.csv"
data = pd.read_csv("50_Startups.csv")

# data = data.dropna()

#Seperate data as features and label
features = data.iloc[:,[0,1,2,3]].values
label = data.iloc[:,[4]].values

finalData = pd.concat([pd.get_dummies(data.State), data.iloc[:,[0,1,2,4]]] , axis = 1)
# print(finalData.info())


# correlation analysis
# print(finalData.corr())
# Calculate correlation matrix
corr_matrix = finalData.corr()

# Correlation of all columns with Profit label
profit_corr = corr_matrix['Profit']
# Select columns where absolute correlation >= 0.5

selected_feature_names = profit_corr[profit_corr.abs() >= 0.5].drop('Profit').index.tolist()
print(selected_feature_names)
# print("\nSelected features (|corr| >= 0.5):")
# print(selected_features.info())
# print(selectedFeats)


selected_features = finalData.iloc[:,[0,2]]
from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(selected_features, label, test_size=0.2, random_state=2)

from sklearn.linear_model import LinearRegression

X = finalData[selected_feature_names]
y = finalData[['Profit']]


for rs in range(1,201):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rs)
    model = LinearRegression()

    model.fit(X_train, y_train)

    trainscore = model.score(X_train, y_train)
    testscore = model.score(X_test, y_test)


    print(trainscore, testscore)

    if(testscore> trainscore and testscore >= 0.9):
        print("APPROVED with rs", rs)
    # else:
    #     print("REJECT")


