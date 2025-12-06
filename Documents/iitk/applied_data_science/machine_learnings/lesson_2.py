import pandas as pd
import numpy as np


csv_file = r"Salary_Data.csv"
data = pd.read_csv(csv_file)

data = data.dropna()

# print(data.info())

# features - yoe
# label - salary
# label type - continouse ND
# algorithm type - regression

# print(data.describe())

# import seaborn as sns
# print(sns.displot(data["YearsExperience"], kind="kde"))

features = data.iloc[:,[0]].values
label = data.iloc[:,[1]].values

# print(features.ndim, label.ndim) check if it 2D

# split the data as training set and testing set
# train_test_split --> returns X_train (training fetaure set), X_test(testing feature set),
# y_train(training label set), y_test(testing label set)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=39)


# print(X_train)

# Initialise the algo --> LinearRegression

from sklearn.linear_model import LinearRegression

model = LinearRegression()

# starts the training
model.fit(X_train, y_train)

CL = 0.95

# print(model.coef_) #b1
# print(model.intercept_) #b0

# print(model.intercept_ + model.coef_ * 2)

# check the quality of the model
# use SL (significance level) ---> 0.05
# CL = 1-SL (0.95)


# when it comes to approve the model, always go for GENERALISED Model

# generalised model is a trained model that not only performs BEST with known data
# but also performs BEST with unknowns data
# model understands POPULATION's patter

# Overfitted model --> works best with known data, but may clutter with unknown data
# calculate the evalution score of the model for both training and testing data
# check the below criteria if testscore > trainscore and testscore >=CL --> approve else no

trainscore = model.score(X_train, y_train)
testscore = model.score(X_test, y_test)


print(trainscore, testscore)

if(testscore> trainscore and testscore >= 0.95):
    print("APPROVED")
else:
    print("REJECT")


# for rs in range(1,101):
#     X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=rs)
#     model = LinearRegression()
#     model.fit(X_train, y_train)

#     trainscore = model.score(X_train, y_train)
#     testscore = model.score(X_test, y_test)

#     if(testscore > trainscore and testscore>=CL):
#         print("Test score: {} and random state:{}", testscore, rs)