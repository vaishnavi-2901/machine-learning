import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = pd.read_csv("50_Startups.csv")

features = data.iloc[:,[0,1,2,3]].values
label = data.iloc[:,[4]].values

# finalData.info()
# print(pd.get_dummies(data.State))

# Do OHE
finalData = pd.concat([pd.get_dummies(data.State), data.iloc[:,[0,1,2,4]]] , axis = 1)
print(finalData.head())

features = finalData.iloc[:,[0,1,2,3,4,5]].values
label = finalData.iloc[:,[6]].values

#step 1: perform all in
featuresAllIn = np.append(np.ones((len(finalData), 1)). astype(int), features, axis=1)
# print(featuresAllin)

# step 2: decide the SL
sl = 0.05

# step 3: perform ols
# endog --> label column
# exog --> feature columns

import statsmodels.regression.linear_model as stat

# olsFormula = stat.OLS(endog = label, exog = featuresAllIn.astype("float") ).fit()

# print(olsFormula.summary())

# step 4: select the feature col that has the highest p-value

# selected feature col is adminSpend(x5) as highest p-value 0.608

# step 5
# check below condition
# if pvalue>SL: 
# eliminate x5
# else: 
# preserve and goto step 7
# since pvalue is greater than SL, therefore eliminate x5

# newFeatureSet = featuresAllIn[:,[0,1,2,3,4,6]]

# olsFormula = stat.OLS(endog=label, exog=newFeatureSet.astype("float")).fit()

# print(olsFormula.summary())

# get highest   P>|t| value in the new summary along with the feature name
# pvalues = olsFormula.pvalues
# print(pvalues) 
# maxPvalue = max(pvalues)
# print("Max P-Value:", maxPvalue)
# featureIndex = np.argmax(pvalues)
# print("Feature Index with Max P-Value:", featureIndex)
pvalue = sl
olsFormula = stat.OLS(endog=label, exog=featuresAllIn.astype("float")).fit()
newFeatureSet = featuresAllIn

while pvalue >= sl:
    pvalues = olsFormula.pvalues
    maxPvalue = pvalues.max()
    if maxPvalue >= sl:
        maxPvalueIndex = np.argmax(pvalues)
        newFeatureSet = np.delete(newFeatureSet, maxPvalueIndex, axis=1)
        olsFormula = stat.OLS(endog=label, exog=newFeatureSet.astype("float")).fit()
        pvalue = maxPvalue
    else:
        break

print(olsFormula.summary())