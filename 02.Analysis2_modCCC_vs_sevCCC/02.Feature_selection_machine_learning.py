# 0. Load library
from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.feature_selection import RFE
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm

# 1. Load data
rawData = pd.read_csv("02.Analysis2_modCCC_vs_sevCCC/01.Feature_selection_percent_methylation/MOD_vs_SEV_train.txt", sep = "\t")
y = rawData.iloc[:,-1]
X = rawData.iloc[:,0:-1]

# 2. Define functions to perform Recursive Feature Extraction and test the resulting model

    # 2.1. Perform RFE
def get_models(myModel, myEstimator, myImportance):
	models = dict()
	for i in range(2, len(X.columns), 1):
		rfe = RFE(estimator=myEstimator, n_features_to_select=i, importance_getter=myImportance)
		model = myModel
		models[str(i)] = Pipeline(steps=[('s',rfe),('m',model)])
	return models
 
    # 2.2. Test model
def evaluate_model(model, X, y):
	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=1, random_state=1)
	scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
	return scores
 
# 3. Perform RFE for different models

    # 3.1. Decision tree
mod = DecisionTreeClassifier()
est = DecisionTreeClassifier()
imp = 'auto'
models = get_models(mod, est, imp)
# Evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
	scores = evaluate_model(model, X, y)
	results.append(scores)
	names.append(name)
df = pd.DataFrame(data = results, 
                  index = names)
# Write the results
df.to_csv("02.Analysis2_modCCC_vs_sevCCC/02.Feature_selection_machine_learning/MOD_SEV_DecisionTree.txt", sep = "\t")

    # 3.2. Random forest
mod = RandomForestClassifier()
est = RandomForestClassifier()
imp = 'auto'
models = get_models(mod, est, imp)
# Evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
	scores = evaluate_model(model, X, y)
	results.append(scores)
	names.append(name)
df = pd.DataFrame(data = results, 
                  index = names)
# Write the results
df.to_csv("02.Analysis2_modCCC_vs_sevCCC/02.Feature_selection_machine_learning/MOD_SEV_RandomForest.txt", sep = "\t")

    # 3.3. Logistic regression
mod = LogisticRegression()
est = LogisticRegression()
imp = 'auto'
models = get_models(mod, est, imp)
# Evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
	scores = evaluate_model(model, X, y)
	results.append(scores)
	names.append(name)
df = pd.DataFrame(data = results, 
                  index = names)
# Write the results
df.to_csv("02.Analysis2_modCCC_vs_sevCCC/02.Feature_selection_machine_learning/MOD_SEV_LogisticRegression.txt", sep = "\t")

    # 3.4. SVM
mod = svm.SVC()
est = svm.SVC(kernel='linear')
imp = 'coef_'
models = get_models(mod, est, imp)
# Evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
	scores = evaluate_model(model, X, y)
	results.append(scores)
	names.append(name)
df = pd.DataFrame(data = results, 
                  index = names)
# Write the results
df.to_csv("02.Analysis2_modCCC_vs_sevCCC/02.Feature_selection_machine_learning/MOD_SEV_SVM.txt", sep = "\t")


