import pickle

from flask import Flask
from flask import request
from flask import jsonify

import xgboost as xgb

model_file = 'final_model.bin'

print(f'Loading the model and DictVectorizer from {model_file}')

#Load dv and Model
with open(model_file, 'rb') as f_model:
    dv, model = pickle.load(f_model)

print('Model and dv Loaded!')

app = Flask('churn')

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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1208)
