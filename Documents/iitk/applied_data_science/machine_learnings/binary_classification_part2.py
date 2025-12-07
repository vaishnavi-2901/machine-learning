"""
classification dataset -- [balanced dataset, un(im)balanced dataset]
balanced dataset: no of records for each unique label is equal. eg: email spam classification dataset
df.label.value_counts()
ham 50
spam 50

un(im)balanced dataset: no of records for each unique lable is different. eg: email spam notification (100 records)
df.label.value_counts()
ham 40
spam 60
evaluation metrics for supervised learning (to check the quality of trained model)
- regression:
    - r^2 score 
- classification:
    - accuracy
    - precision
    - recall
    - f1-score

when to use which evalution metric for classification?
1. check if your dataset is balanced or unbalanced
2. if balaced dataset, use accurancy (default metric) wrt total dataset --> for generalisation and CL check also
3. else, statistical (binary and multiclass) --> 
accuracy (filter generalised model), f1-score (CL check with entire dataset)
or domain approach (usually done for binary classification) --> 
accuracy (filter generalised model), PR (precision recall) pair (for CL check with entire dataset)


Confusion Metric --> error metric in a tabular form to visualise the performance of the classification model
eg: emailSpam.csv 

"""
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")


data = pd.read_csv('Social_Network_Ads.csv')
# print(data.info())

# assume 0- bad customer, 1- good customer
features = data.iloc[:,[0,1]].values
label = data.iloc[:,[2]].values 

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


# final model

X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=220)
model1 = LogisticRegression()
model1.fit(X_train, y_train)

from sklearn.metrics import confusion_matrix as confusion_metrix
print(confusion_metrix(label, model1.predict(features)))

import pickle
pickle.dump(model, open("classification.pk", "wb"))

model2 = pickle.load(open("classification.pk", "rb"))

# Two possibilities
# Assume
# 0 --- Bad customer (Customer will not make a purchase --- Window shopping ;) )
# 1 --- Good customer ( Customer will make a purchase )

# 1. 0Bad customer ---- 1Good customer
# 2. 1Good customer ---- 0Bad customer

# P0 -- 0.85
# R1 -- 0.71
#
# macroAvg = 0.78 not greater than 0.95 --- DISCARD


from sklearn.metrics import classification_report
print(classification_report(label,model.predict(features)))