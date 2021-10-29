import pickle

from flask import Flask
from flask import request
from flask import jsonify

import xgboost as xgb

model_file = 'final_model.bin'
dir = 'mysite'

#Load dv and Model
with open(f'{dir}/{model_file}', 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('subscribe')

@app.route('/predict', methods=['POST'])
def predict():
    print('Getting customer data...')
    customer = request.get_json()
    print('Customer data received!')
    X = dv.transform([customer])

    features = dv.get_feature_names()
    dcust = xgb.DMatrix(X, feature_names=features)
    #Predict
    print('Predicting Subscribe Probability......')
    y_pred = model.predict(dcust)[:].round(4)
    subs = y_pred >= 0.5
    print('Subscribe probability: ', y_pred)

    result = {
        "Subscribe Probability": float(y_pred),
        "Subscribe": bool(subs)
    }
    print('Prediction result sent!')
    return jsonify(result)
