import requests

url = "http://localhost:1208/predict_with_flask_hw5"

customer_id = 'aed-313'
customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}


response = requests.post(url, json=customer).json()
print(response)

if response["Churn"] == True:
    print('Sending promo email to %s' % customer_id)
else:
    print('Not sending promo email to %s' % customer_id)