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
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn import datasets, metrics, model_selection, svm
from sklearn.metrics import roc_auc_score

# 1. Load data

	# 1.1. Train
rawDataTrain = pd.read_csv("02.Analysis2_modCCC_vs_sevCCC/01.Feature_selection_percent_methylation/MOD_vs_SEV_train.txt", sep = "\t")
y_train = rawDataTrain.iloc[:,-1]
X_train = rawDataTrain.iloc[:,0:-1]

	# 1.2. Test
rawDataTest = pd.read_csv("02.Analysis2_modCCC_vs_sevCCC/01.Feature_selection_percent_methylation/MOD_vs_SEV_test.txt", sep = "\t")
y_test = rawDataTest.iloc[:,-1]
X_test = rawDataTest.iloc[:,0:-1]


# 2. Select features according to the best model - features combinations find in the step 2

    # 2.1. Define and fit RFE
rfe = RFE(estimator=RandomForestClassifier(random_state=42), n_features_to_select=33)
rfe.fit(X_train, y_train)

    # 2.2. Select the features
index = list()
selection = list()
rank = list()
for i in range(X_train.shape[1]):
	index.append(i)
	selection.append(rfe.support_[i])
	rank.append(rfe.ranking_[i])
df = pd.DataFrame(list(zip(index, selection, rank)),
					columns = ["Index", "Selection", "Rank"])
myIndex=df.loc[df['Selection'] == True, 'Index'].tolist()

    # 2.3. Reduce train and test dataset with the selected features on train dataset
X_train2 = X_train.iloc[:,myIndex]
X_test2 = X_test.iloc[:,myIndex]


# 3. Create the model and find best parameters
model=RandomForestClassifier(random_state=42)
param_grid = { 
    'n_estimators': [50, 100, 150, 200],
    'criterion' :['entropy']
}
CV_model = GridSearchCV(estimator=model, param_grid=param_grid, cv= 10, n_jobs = 4)
CV_model.fit(X_train2, y_train)
print(CV_model.best_params_)
bestP = CV_model.best_params_

# 4. Apply model with best parameters
model = RandomForestClassifier(n_estimators = bestP['n_estimators'], criterion = 'entropy', class_weight = 'balanced', random_state=42)
model = model.fit(X_train2,y_train)
y_pred = model.predict(X_test2)
print("Accuracy:",accuracy_score(y_test, y_pred))

# 5. Save the predictions in a dataframe
df = pd.DataFrame(list(zip(y_test, y_pred)),
					columns = ["Test", "Prediction"])
df.to_csv("02.Analysis2_modCCC_vs_sevCCC/03.Model_evaluation_optimization/MOD_SEV_prediction.tab", sep = "\t")

# 6. Plot ROC curves
fpr, tpr, thresholds = roc_curve(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred)
    # 6.1. Generate a no skill prediction (majority class)
ns_probs = [0 for _ in range(len(y_test))]
    # 6.2. Predict probabilities
lr_probs = model.predict_proba(X_test2)
    # 6.3. Keep probabilities for the positive outcome only
lr_probs = lr_probs[:, 1]
    # 6.4. Calculate scores
ns_auc = roc_auc_score(y_test, ns_probs)
lr_auc = roc_auc_score(y_test, lr_probs)
    # 6.5. Calculate roc curves
ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)
lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs)
    # 6.6. Plot the roc curve for the model
plt.plot(ns_fpr, ns_tpr, linestyle='--', color = "black")
plt.plot(lr_fpr, lr_tpr, marker='.', label='Logistic: ROC curve (area=%.3f)' % (lr_auc), color = "blue")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.savefig('02.Analysis2_modCCC_vs_sevCCC/03.Model_evaluation_optimization/ROC_curve.pdf')

