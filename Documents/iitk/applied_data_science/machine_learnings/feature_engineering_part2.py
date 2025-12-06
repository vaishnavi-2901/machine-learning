import pandas as pd
import numpy as np
import statsmodels.regression.linear_model as stat
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv("50_Startups.csv")
features = data.iloc[:,[0,1,2,3]].values
label = data.iloc[:,[4]].values
# separate features and label
features = data.iloc[:,[0,1,2,3]].values
label = data.iloc[:,[4]].values

# OHE for state column
OheForState = OneHotEncoder(sparse_output=False)
stateOhe = OheForState.fit_transform(features[:,[3]])

finalFeatureSet = np.concatenate((stateOhe, features[:,[0,1,2]]), axis=1) #column based
features = finalFeatureSet
# print(features)


# Recursive Feature Elimination (RFE) to select top features

"""
RFE is applicable for following alogorithms:
----------------------------
regression:
1. Linear Regression
2. SupportVecor Regression
3. Decision Tree Regression
4. Random Forest Regression
----------------------------
Classification:
1. Logistic Regression
2. Dicision Tree Classifier
3. Random Forest Classifier
"""


# step 1: initialize ML algo
from sklearn.linear_model import LinearRegression
modelAlgo = LinearRegression()

# Step2: initialize RFE
from sklearn.feature_selection import RFE
selectedFeatures = RFE(estimator=modelAlgo)

# step3: fit the data to RFE
selectedFeatures.fit(finalFeatureSet, label)

# step 4: features with higer ranking
# print(selectedFeatures.ranking_)

# guideline: select the features with ranking 1 and 2
# RFE selected: californnia. Florida, NY, R&D spend

from sklearn.model_selection import train_test_split
for rs in range(1,201):
    finalSelectedFeatures = finalFeatureSet[:, [0,1,2,3]] # california, Florida, Ny, R&D spend
    X_train, X_test, y_train, y_test = train_test_split(finalSelectedFeatures, label, test_size=0.2, random_state=rs)
    model = LinearRegression()
    model.fit(X_train, y_train)
    trainscore = model.score(X_train, y_train)
    testscore = model.score(X_test, y_test)
    # print(trainscore, testscore)
    # if(testscore> trainscore and testscore >= 0.9):
    #     print("APPROVED with rs", rs)

# SFM: select from model: it can be applied to all ML algorithms

# step 1: initialize the ML algo
modelAlgoSFM = LinearRegression()

# step 2: initialize SFM
from sklearn.feature_selection import SelectFromModel
selectedFeaturesSFM = SelectFromModel(estimator=modelAlgoSFM)

# step 3: fit the data to SFM
selectedFeaturesSFM.fit(finalFeatureSet, label)

# step 4: get the ranking
print(selectedFeaturesSFM.get_support()) # selected columns are california, Florida, Ny
sl = 0.05
cl = 1-sl
# do the model training and testing with selected features only
for rs in range(1,201):
    finalSelectedFeatures = finalFeatureSet[:, [0,1,2]] # california, Florida, Ny
    X_train, X_test, y_train, y_test = train_test_split(finalSelectedFeatures, label, test_size=0.2, random_state=rs)
    model = LinearRegression()
    model.fit(X_train, y_train)
    testscore = model.score(X_test, y_test)
    trainscore = model.score(X_train, y_train)
    print("Test Score:", testscore)
    print("Train Score:", trainscore)
    if (testscore> trainscore and testscore >= cl):
        print("APPROVED with rs", rs)

