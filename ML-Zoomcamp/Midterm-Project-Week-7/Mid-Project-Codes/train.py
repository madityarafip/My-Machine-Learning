# Library
import pandas as pd
import numpy as np

from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier

import xgboost as xgb

import pickle

# Parameter
eta = 0.5
d = 10
w = 1
output_file = 'final_model.bin'

print('Preparing data.....')
# Data Preparation
df = pd.read_csv('bank-full.csv')

used_cols = ['age', 'marital', 'job', 'default', 'balance', 'housing',
             'loan', 'campaign', 'previous', 'Target'
            ]
df_proj = df[used_cols].copy()

df_proj['target_cat'] = (df_proj.Target == 'yes').astype(int)
del df_proj['Target']

# Data Balancing
## Class count
count_class_0, count_class_1 = df_proj.target_cat.value_counts()

## Divide by class
df_proj_0 = df_proj[df_proj['target_cat'] == 0]
df_proj_1 = df_proj[df_proj['target_cat'] == 1]

df_proj_1_over = df_proj_1.sample(count_class_0, replace=True)
df_proj_new = pd.concat([df_proj_0, df_proj_1_over], axis=0)


numerical = ['age', 'balance', 'campaign', 'previous']
categorical = ['marital', 'job', 'default', 'housing', 'loan']
print('Data Ready!')

print(' ')

print('Split data -> train/val/test (60%/20%/20%)')
# Split Data
#80% Full Train, 20% Test
df_full_train, df_test = train_test_split(df_proj_new, test_size=0.2, random_state=15)
#60% Train, 20% Val (25% from Full Train -> 20%/80%)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=15)

y_train = df_train.target_cat.values
y_val = df_val.target_cat.values
y_test = df_test.target_cat.values

del df_train['target_cat']
del df_val['target_cat']
del df_test['target_cat']


print('Train Full:', len(df_full_train), 
      '(', round((len(df_full_train)/len(df_proj_new))*100, 2), '%)') 
print('Train:', len(df_train), 
      '(', round((len(df_train)/len(df_proj_new))*100, 2), '%)') 
print('Validation:', len(df_val), 
      '(', round((len(df_val)/len(df_proj_new))*100, 2), '%)') 
print('Test:', len(df_test), 
      '(', round((len(df_test)/len(df_proj_new))*100, 2), '%)')


# OHE using DV
def OHE_DV(df, dv, col):
    dicts = df[col].to_dict(orient='records')
    X_data = dv.fit_transform(dicts)
    
    return X_data
#-------------------------------------------------------#
def OHE_DV_wo_fit(df, dv, col):
    dicts = df[col].to_dict(orient='records')
    X_data = dv.transform(dicts)
    
    return X_data

print(' ')
# Model Validation
print('Validation Process Start....')
dv = DictVectorizer(sparse=False)

X_col = categorical+numerical 

X_train = OHE_DV(df_train, dv, X_col)
X_val = OHE_DV_wo_fit(df_val, dv, X_col)

# Matrix for XGBoost
features = dv.get_feature_names()
dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=features)
dval = xgb.DMatrix(X_val, label=y_val, feature_names=features)

# Model using XGBoost
xgb_params = {
    'eta': eta, 
    'max_depth': d,
    'min_child_weight': w,
    
    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
    }

model = xgb.train(xgb_params, dtrain, num_boost_round=200) 

y_pred = model.predict(dval)
auc = roc_auc_score(y_val, y_pred)

print('Validation result:')
print('AUC on validation: ', auc.round(3))

print(' ')
# Train Final Model
print('Training Final Model Start!')
y_full_train = df_full_train.target_cat.values

del df_full_train['target_cat']

dv = DictVectorizer(sparse=False)

X_col = categorical+numerical 

X_full_train = OHE_DV(df_full_train, dv, X_col)
X_test = OHE_DV_wo_fit(df_test, dv, X_col)

features = dv.get_feature_names()
dfull_train = xgb.DMatrix(X_full_train, label=y_full_train, feature_names=features)
dtest = xgb.DMatrix(X_test, label=y_test, feature_names=features)

xgb_params = {
    'eta': eta, 
    'max_depth': d,
    'min_child_weight': w,
    
    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
    }

model_final = xgb.train(xgb_params, dfull_train, num_boost_round=200)

y_pred = model_final.predict(dtest)
auc_final = roc_auc_score(y_test, y_pred)
print('Training Final Model Finish!')
print('Final Model -> AUC Score = ', auc_final.round(3))

# Save the model
print('Save Model....')

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model_final), f_out)

print('The model is saved to ', output_file)
