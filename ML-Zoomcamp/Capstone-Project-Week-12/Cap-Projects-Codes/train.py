# Library
import pandas as pd
import numpy as np

from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier

from math import ceil

import xgboost as xgb

import pickle

# Parameter
eta = 0.1
d = 6
w = 1
output_file = 'final_model.bin'

# Get Dataset
print('Preparing data.....')
data = 'weatherAUS.csv'

df = pd.read_csv(data)

# Data Preparation
## Change Date feature into DateTime
df['Date'] = pd.to_datetime(df['Date'])

## Create new features from Date feature (Day, Month, Year)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

## Change Month feature into Categorical
month_values = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'Desember'
}
df.Month = df.Month.map(month_values) 
print('Data Ready!')

print(' ')

print('Split data -> train/val/test (60%/20%/20%)')
def train_test_split_dates_sorted(df, test_size, dates):
    n_test = ceil(test_size * len(df))

    sorted_index = [x for _, x in sorted(zip(np.array(dates), np.arange(0, len(dates))), key=lambda pair: pair[0])]
    train_idx = sorted_index[:-n_test]
    test_idx = sorted_index[-n_test:]

    if isinstance(df, (pd.Series, pd.DataFrame)):
        df_train = df.iloc[train_idx]
        df_test = df.iloc[test_idx]
    else:
        df_train = df[train_idx]
        df_test = df[test_idx]

    return df_train, df_test  

df_full_train, df_test = train_test_split_dates_sorted(df, 0.2, df['Date'])
df_train, df_val = train_test_split_dates_sorted(df_full_train, 0.25, df_full_train['Date'])

print('Train Full:', len(df_full_train), 
      '(', round((len(df_full_train)/len(df))*100, 2), '%)') 
print('Train:', len(df_train), 
      '(', round((len(df_train)/len(df))*100, 2), '%)') 
print('Validation:', len(df_val), 
      '(', round((len(df_val)/len(df))*100, 2), '%)') 
print('Test:', len(df_test), 
      '(', round((len(df_test)/len(df))*100, 2), '%)') 


for df1 in [df_full_train, df_train, df_val, df_test]:
    df1.drop('Date', axis=1, inplace = True)

print(' ')

# Get Numerical and Categorical Feature
def get_cat_num_feat(df):
    categorical = [col for col in df.columns if df[col].dtype=='O']
    numerical = [col for col in df.columns if df[col].dtype!='O']
    
    return categorical, numerical

categorical, numerical = get_cat_num_feat(df_full_train)

print(f'There are {len(categorical)} categorical features')
print('The categorical features are :', categorical)

print('')

print(f'There are {len(numerical)} numerical features')
print('The numerical features are :', numerical)

print(' ')
# Feature Engineering
## Deal with missing value
### Numerical
for df3 in [df_full_train, df_train, df_val, df_test]:
    for col in numerical:
        col_median=df_full_train[col].median()
        df3[col].fillna(col_median, inplace=True)   

### Categorical
for df4 in [df_full_train, df_train, df_val, df_test]:
    for col in categorical:
        freq_val = df_full_train[col].mode()[0]
        df4[col].fillna(freq_val, inplace=True)

# Deal with outlier
def max_value(df, feature, top):
    top_code = np.where(df[feature]>top, top, df[feature])
    return top_code

df_name = ['df_full_train', 'df_train', 'df_val', 'df_test']
out_col = ['Rainfall', 'Evaporation', 'WindGustSpeed',
           'WindSpeed9am', 'WindSpeed3pm']
value_max = [3.2, 21.0, 99.0, 55.0, 57.0]

for df6, dname in zip([df_full_train, df_train, df_val, df_test], df_name):
    print(f'Dealing with outliers at {dname}')
    for col, val in zip(out_col, value_max):
        df6[col] = max_value(df6, col, val)
        print(f'Max and Min values for {col} are {df6[col].max()} and {df6[col].min()}')
    print('---------------------------------------------------------------------')

print(' ')
# Declare Features for Projects
for df7 in [df_full_train, df_train, df_val, df_test]:
    df7['target_cat'] = (df7.RainTomorrow == 'Yes').astype(int)
    del df7['RainTomorrow']    

y_full_train = df_full_train.target_cat.values
y_train = df_train.target_cat.values
y_val = df_val.target_cat.values
y_test = df_test.target_cat.values

for df8 in [df_train, df_val]:
    df8.drop('target_cat', axis=1, inplace = True)

categorical, numerical = get_cat_num_feat(df_train)

print(f'There are {len(categorical)} categorical features')
print('The categorical features are :', categorical)

print('')

print(f'There are {len(numerical)} numerical features')
print('The numerical features are :', numerical)

# OHE with DictVectorizer()
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

print('The model is saved to', output_file)
