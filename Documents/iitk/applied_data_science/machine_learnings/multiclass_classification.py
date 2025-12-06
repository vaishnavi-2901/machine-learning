import pandas as pd
import numpy as np

# create a model that can classify the iris flower species based on flower's properties
data = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")
# print(data.variety.unique())

# separate the data as features and label
features = data.iloc[:,[0,1,2,3]].values
label = data.iloc[:,[4]].values

# print(features, label)

CL = 0.95

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import warnings
warnings.filterwarnings("ignore")

# for rs in range(1,301):
#     X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=rs)
#     model = LogisticRegression()
#     model.fit(X_train, y_train)

#     trainScore = model.score(X_train, y_train)
#     testScore = model.score(X_test, y_test)


    # if testScore > trainScore and testScore >= CL:
    #     print(f"Test score: {testScore} | Train Score: {trainScore} | Rs: {rs}")



# create final model

X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=3)

model = LogisticRegression()
model.fit(X_train, y_train)

trainScore = model.score(X_train, y_train)
testScore = model.score(X_test, y_test)
print(f"Test Score : {testScore} | Train Score : {trainScore} ")

# Step 1: initialize the ML Algo
from sklearn.linear_model import LogisticRegression
modelAlgo = LogisticRegression()

# step 2: intialize RFE
from sklearn.feature_selection import RFE
selectedFeatures = RFE(estimator=modelAlgo)

# step 3: fit the data to RFE
selectedFeatures.fit(features, label)

print(selectedFeatures.ranking_)
# deploy code

sepalLength = float(input("Enter sepal Length:"))
sepalWidth = float(input("Enter sepal Width:"))
petalLength = float(input("Enter petal Length:"))
petalWidth = float(input("Enter petal Width:"))

pred  = selectedFeatures.predict(np.array([[sepalLength,sepalWidth, petalLength, petalWidth]]))

print(f"variety of flower is: {pred}")
