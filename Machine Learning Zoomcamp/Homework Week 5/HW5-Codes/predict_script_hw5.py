import pickle

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}
#customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}
model_file = 'model1.bin'
dv_file = 'dv.bin'
customer_id = 'aed-313'

print(f'Loading the model from {model_file} and the DictVectorizer from {dv_file}')

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
churn = y_pred >= 0.5
print('Churn probability: ', round(y_pred, 3))
if churn == True:
    print('Sending promo email to %s' % customer_id)
else:
    print('Not sending promo email to %s' % customer_id)
