import pickle

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}
#customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}
model_file = 'model1.bin'
dv_file = 'dv.bin'
print(f'Loading the model from {model_file} and the dv from {dv_file}')

#Load dv and Model
with open(dv_file, 'rb') as f_dv:
    dv = pickle.load(f_dv)
with open(model_file, 'rb') as f_model:
    model = pickle.load(f_model)

print('Model and dv Loaded!')
print(' ')
print('Input Customer -> ', customer)
X = dv.transform(customer)

#Predict

y_pred = model.predict_proba(X)[0,1]
print('Churn probability: ', round(y_pred, 3))
