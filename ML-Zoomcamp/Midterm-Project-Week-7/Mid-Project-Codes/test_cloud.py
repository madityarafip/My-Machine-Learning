import requests
import json

url = "http://madityarafip.pythonanywhere.com/predict"


print('Fill potential client data below:')
print('#--------------------------------------------------------------------------------------------------------------------------#')
customer_id = input('Customer ID: ')
age = int(input('Age: '))
print('Marital Status? (divorced, married, single, unknown)')
marital = input('Input: ')
print('Job? (admin, bluecollar, entrepreneur, housemaid, management, retired, selfemployed, services, student, technician, unemployed, unknown)')
job = input('Input: ')
print('Has credit in default? (yes, no, unknown)')
default = input('Input: ')
balance = int(input('Balance: '))
print('Has housing loan? (yes, no, unknown)')
housing = input('Input: ')
print('Has Personal loan? (yes, no, unknown)')
loan = input('Input: ')
campaign = int(input('Number of contacts performed during this campaign and for this client: '))
previous = int(input('Number of contacts performed before this campaign and for this client: '))

client_data = {
            "age": age, 
            "marital": marital,
            "job": job, 
            "default": default, 
            "balance": balance, 
            "housing": housing,
            "loan": loan, 
            "campaign": campaign, 
            "previous": previous
             }


response = requests.post(url, json=client_data).json()
print(response)

if response["Subscribe"] == True:
    print('Sending subscribe offer email to %s' % customer_id)
else:
    print('Not sending subscribe offer email to %s' % customer_id)
