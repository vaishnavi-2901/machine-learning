import pandas as pd
import numpy as np

data = pd.read_csv('Social_Network_Ads.csv')
# print(data.info())

# assume 0- bad customer, 1- good customer
features = data.iloc[:,[0,1]].values
label = data.iloc[:,[2]].values

import warnings
warnings.filterwarnings("ignore")

cl = 0.95
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression # for binary classification label
for rs in range(1, 301):
    X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=rs)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    trainScore  = model.score(X_train, y_train)
    testScore = model.score(X_test, y_test)
    if testScore > trainScore and testScore>=cl:
        print(f"test score: {testScore} | train score: {trainScore} | RS: {rs}")

# commit the model in a file (pickle) and then create sample code to show dev how to use the model
# deploy phase



import pickle
pickle.dump(model, open("customerPredictor.pk", "wb"))

model2 = pickle.load(open("customerPredictor.pk", "rb"))
age = int(input("Enter age"))
estimated_salary = float(input("Enter Salary"))

result = model2.predict(np.array([[age, estimated_salary]]))
if 1 in result:
    print("Customer is good: ", result)
else:
    print("Customer is bad: ", result)