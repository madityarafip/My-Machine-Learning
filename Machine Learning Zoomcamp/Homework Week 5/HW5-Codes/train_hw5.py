#Library
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline

from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

import pickle

#Parameters
n_splits = 5
output_file = f'model_train.bin'

#Data Preparation
print('Preparing data.....')
df = pd.read_csv('data-week-3.csv')
df.head(3)

df.columns = df.columns.str.lower().str.replace(' ', '_')

categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')

tc = pd.to_numeric(df.totalcharges, errors='coerce')

df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')

df.totalcharges = df.totalcharges.fillna(0)

df.churn = (df.churn == 'yes').astype(int)
print('Data Ready!')

#Split Data
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

y_test = df_test.churn.values

#Train and Validate Model
def train(df_train, y_train, col):
    dicts = df_train[col].to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    model = LogisticRegression(solver='liblinear', C=1, max_iter=1000).fit(X_train, y_train)
    
    return dv, model
#--------------------------------------------------------------------------
def predict(df, dv, model, col):
    dicts = df[col].to_dict(orient='records')
    
    X_data = dv.transform(dicts)
    y_pred = model.predict_proba(X_data)[:, 1]

    return y_pred

#Validate the Model
col = ['tenure', 'monthlycharges', 'contract']

print('Doing Validation Process....')
kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)
scores = []
fold = 0
for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train.churn.values
    y_val = df_val.churn.values

    dv, model = train(df_train, y_train, col)
    y_pred = predict(df_val, dv, model, col)

    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)

    print(f'AUC on fold {fold} is {auc}')
    fold += 1

print('Validation Result -> Mean = %.3f | STD = +- %.3f' % (np.mean(scores), np.std(scores)))

#Train Final Model (Test)
print('Final Train Model Start!')

dv, model = train(df_full_train, df_full_train.churn.values, col)
y_pred_final = predict(df_test, dv, model, col)

print('Final Train Model Finish!')
auc_final = roc_auc_score(y_test, y_pred_final)

print(f'AUC final is {round(auc_final, 3)}')

#Save Model
print('Save Model....')
with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)
print(f'The model is saved to {output_file}')