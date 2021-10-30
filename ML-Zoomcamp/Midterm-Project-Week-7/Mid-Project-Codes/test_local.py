import requests
import json

url = "http://localhost:1208/predict"


print('  \nFill potential client data below:')
print('#------------------------------------------------------------------------#')
customer_id = input('Customer ID: ')
age = int(input('Age: '))
print('Marital Status? (divorced, married, single, unknown)')
marital = input('Input: ')
print('Job? (admin, bluecollar, entrepreneur, housemaid, management, retired, selfemployed, services, student, technician, unemployed, unknown)')
job = input('Input: ')
print('Has credit in default? (yes, no, unknown)')
default = input('Input: ')
balance = int(input('Balance (euro): '))
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
print(' ')
print(f'Please wait..\nSending client data with ID:{customer_id} to Subscription Services.....')
response = requests.post(url, json=client_data).json()
pred = (response["Subscribe Probability"]*100)
print(' \nGeting the response...\n  ')
print(f'Potential client with ID:{customer_id} have a subscription probability of {round(pred, 2)}%')

print('\nSuggestion from Subscription Services system')
if response["Subscribe"] == True:
    print(f'--> Send email of a deposit term subscription offer to a potential client with ID:{customer_id}')
else:
    print(f"--> Don't need to send email of a deposit term subscription offer to a potential client with ID:{customer_id}")
