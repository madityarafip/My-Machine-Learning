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

app = Flask('rain-pred')

@app.route('/welcome', methods=['GET'])
def welcome():
    welcome_msg = "<h1>Welcome! Your application is succesfully deployed as Docker container on heroku</h1>"
    return welcome_msg

@app.route('/predict', methods=['POST'])
def predict():
    print('Getting data...')
    rain_data = request.get_json()
    print('Data is received!')
    X = dv.transform([rain_data])
    features = dv.get_feature_names()
    dpred = xgb.DMatrix(X, feature_names=features)
    #Predict
    print('Predicting Rain Tomorrow Probability......')
    y_pred = model.predict(dpred)[0]
    subs = y_pred >= 0.6
    print(f'Rain Tomorrow probability: {(y_pred*100).round(2)} %')

    result = {
        "Rain Tomorrow Probability": float(y_pred),
        "Rain Tomorrow": bool(subs)
    }
    print('Prediction result sent!')
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1208)