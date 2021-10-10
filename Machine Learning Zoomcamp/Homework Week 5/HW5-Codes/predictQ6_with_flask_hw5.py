import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model2.bin'
dv_file = 'dv.bin'

print(f'Loading the model from {model_file} and the dv from {dv_file}')

#Load dv and Model
with open(dv_file, 'rb') as f_dv:
    dv = pickle.load(f_dv)

with open(model_file, 'rb') as f_model:
    model = pickle.load(f_model)

print('Model and dv Loaded!')

app = Flask('churn')

@app.route('/predict_with_flask_hw5', methods=['POST'])
def predict_with_flask_hw5():
    print('Getting customer data...')
    customer = request.get_json()
    print('Customer data received!')
    X = dv.transform([customer])
    #Predict
    print('Predicting Churn Probability......')
    y_pred = model.predict_proba(X)[:, 1].round(4)
    churn = y_pred >= 0.5
    print('Churn probability: ', y_pred)

    result = {
        "Churn Probability": float(y_pred),
        "Churn": bool(churn)
    }
    print('Prediction result sent!')
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1208)

