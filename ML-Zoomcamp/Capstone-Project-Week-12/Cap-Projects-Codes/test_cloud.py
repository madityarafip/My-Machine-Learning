import requests
import json

url = "http://cap-proj-docker.herokuapp.com/predict"

data_test_1 = {
            "Location": "Portland", 
            "MinTemp": 12.7,
            "MaxTemp": 17.3, 
            "Rainfall": 3.2, 
            "Evaporation": 7.6, 
            "Sunshine": 5.9,
            "WindGustDir": "W", 
            "WindGustSpeed": 67.0, 
            "WindDir9am": "SW",
            "WindDir3pm" : "SW",
            "WindSpeed9am" : 26.0,
            "WindSpeed3pm" : 33.0,
            "Humidity9am" : 65.0,
            "Humidity3pm" : 55.0,
            "Pressure9am" : 1001.8,
            "Pressure3pm" : 1007.5,
            "Cloud9am" : 8.0,
            "Cloud3pm" : 8.0,
            "Temp9am" : 14.8,
            "Temp3pm" : 16.0,
            "RainToday" : "Yes",
            "Year" : 2016,
            "Month" : "March",
            "Day" : 18
             }

data_test_2 = {
            "Location": "Uluru", 
            "MinTemp": 26.2,
            "MaxTemp": 39.9, 
            "Rainfall": 0.0, 
            "Evaporation": 4.6, 
            "Sunshine": 3.4,
            "WindGustDir": "W", 
            "WindGustSpeed": 41.0, 
            "WindDir9am": "ENE",
            "WindDir3pm" : "WSW",
            "WindSpeed9am" : 7.0,
            "WindSpeed3pm" : 22.0,
            "Humidity9am" : 44.0,
            "Humidity3pm" : 24.0,
            "Pressure9am" : 1007.1,
            "Pressure3pm" : 1002.6,
            "Cloud9am" : 1.0,
            "Cloud3pm" : 2.0,
            "Temp9am" : 30.8,
            "Temp3pm" : 38.8,
            "RainToday" : "No",
            "Year" : 2016,
            "Month" : "March",
            "Day" : 17
             }

data_test_3 = {
            "Location": "Canberra", 
            "MinTemp": 17.0,
            "MaxTemp": 25.4, 
            "Rainfall": 3.2, 
            "Evaporation": 4.6, 
            "Sunshine": 8.4,
            "WindGustDir": "E", 
            "WindGustSpeed": 46.0, 
            "WindDir9am": "SSE",
            "WindDir3pm" : "NE",
            "WindSpeed9am" : 9.0,
            "WindSpeed3pm" : 26.0,
            "Humidity9am" : 80.0,
            "Humidity3pm" : 55.0,
            "Pressure9am" : 1021.8,
            "Pressure3pm" : 1018.2,
            "Cloud9am" : 5.0,
            "Cloud3pm" : 5.0,
            "Temp9am" : 19.2,
            "Temp3pm" : 25.4,
            "RainToday" : "Yes",
            "Year" : 2017,
            "Month" : "March",
            "Day" : 15
             }


data_test_4 = {
            "Location": "AliceSprings", 
            "MinTemp": 17.8,
            "MaxTemp": 39.8, 
            "Rainfall": 0.0, 
            "Evaporation": 12.8, 
            "Sunshine": 8.4,
            "WindGustDir": "SSE", 
            "WindGustSpeed": 41.0, 
            "WindDir9am": "NE",
            "WindDir3pm" : "S",
            "WindSpeed9am" : 13.0,
            "WindSpeed3pm" : 20.0,
            "Humidity9am" : 21.0,
            "Humidity3pm" : 15.0,
            "Pressure9am" : 1011.2,
            "Pressure3pm" : 1006.9,
            "Cloud9am" : 5.0,
            "Cloud3pm" : 5.0,
            "Temp9am" : 30.6,
            "Temp3pm" : 39.2,
            "RainToday" : "No",
            "Year" : 2017,
            "Month" : "March",
            "Day" : 24
             }

print('  \nChoose test data below:')
print('#------------------------------------------------------------------------#')
print('data_test_1: ')
print(data_test_1)

print('')

print('data_test_2: ')
print(data_test_2)

print('')

print('data_test_3: ')
print(data_test_3)

print('')

print('data_test_4: ')
print(data_test_4)

print('')

while True:
    data_choose = input('Which data you want to use? -> ')

    if data_choose=='data_test_1':
        data = data_test_1
        print('You choose data_test_1!')
    elif data_choose=='data_test_2':
        data = data_test_2
        print('You choose data_test_2!')
    elif data_choose=='data_test_3':
        data = data_test_3
        print('You choose data_test_3!')
    elif data_choose=='data_test_4':
        data = data_test_4
        print('You choose data_test_4!')

    print(' ')
    print(f'Please wait..\nSending test data:{data_choose} to Rain Prediction Services.....')
    response = requests.post(url, json=data).json()
    pred = (response["Rain Tomorrow Probability"]*100)
    print(' \nGeting the response...\n  ')
    print(f'Rain probability: {round(pred, 2)}%')

    print('\nSuggestion from Rain Prediction Services system')
    if response["Rain Tomorrow"] == True:
        print("--> Tomorrow it will rain! Please don't forget to bring your umberella or coat!")
    else:
        print("--> Tomorrow it probably won't rain, have a nice day!")