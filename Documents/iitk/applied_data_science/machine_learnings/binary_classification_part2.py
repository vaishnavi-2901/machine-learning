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