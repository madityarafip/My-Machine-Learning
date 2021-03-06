# **CAPSTONE PROJECT: RAIN PREDICTION IN AUSTRALIA**
This project is part of the [Machine Learning Zoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) training held by [DataTalksClub](https://datatalks.club/). In this Capstone Project, everything that has been learned in the previous weeks was applied in this project. To see what I have learned during this training, you can refer to this following [link](https://github.com/madityarafip/My-Machine-Learning/tree/main/ML-Zoomcamp). The problem raised in this project is the prediction of whether tomorrow will rain or not in Australia based from Australia weather dataset. ('Yes' or 'No' condition).

## **About the Dataset**
### Data Source
For this project I used the dataset from [**Kaggle**](https://www.kaggle.com/jsphyg/weather-dataset-rattle-package)
### Data Description
This dataset contains about 10 years of daily weather observations from numerous Australian weather stations.
### Feature Information
| No. | Feature | Type | Information     |
| --- | --- | --- | --- |
| 1 | Date | Categorical | The date of observation (01-11-2007 to 25-06-2017) |
| 2 | Location | Categorical | The common name of the location of the weather station in Australia |
| 3 | MinTemp | Numerical | Min. Temperature (degrees C) |
| 4 | MaxTemp | Numerical | Max. Temperature (degrees C) |
| 5 | Rainfall | Numerical | The amount of rainfall recorded for the day in mm |
| 6 | Evaporation | Numerical | The so-called Class A pan evaporation (mm) in the 24 hours to 9am |
| 7 | Sunshine | Numerical | The number of hours of bright sunshine in the day |
| 8 | WindGustDir | Categorical | The direction of the strongest wind gust in the 24 hours to midnight |
| 9 | WindGustSpeed | Numerical | The speed (km/h) of the strongest wind gust in the 24 hours to midnight |
| 10 | WindDir9am | Categorical | Direction of the wind at 9am |
| 11 | WindDir3pm | Categorical | Direction of the wind at 3pm |
| 12 | WindSpeed9am | Numerical | Wind speed (km/hr) averaged over 10 minutes prior to 9am |
| 13 | WindSpeed3pm | Numerical | Wind speed (km/hr) averaged over 10 minutes prior to 3pm |
| 14 | Humidity9am | Numerical | Humidity (%) at 9am | 
| 15 | Humidity3pm | Numerical | Humidity (%) at 3pm |
| 16 | Pressure9am | Numerical | Atmospheric pressure (hpa) reduced to mean sea level at 9am |
| 17 | Pressure3pm | Numerical | Atmospheric pressure (hpa) reduced to mean sea level at 3pm |
| 18 | Cloud9am | Numerical | Fraction of sky obscured by cloud at 9am. This is measured in "oktas", which are a unit of eigths. It records how many |
| 19 | Cloud3pm | Numerical | Fraction of sky obscured by cloud at 3pm. This is measured in "oktas", which are a unit of eigths. It records how many |
| 20 | Temp9am | Numerical | Temperature (degrees C) at 9am |
| 21 | Temp3pm | Numerical | Temperature (degrees C) at 3pm |
| 22 | RainToday | Categorical | Boolean: 1 if precipitation (mm) in the 24 hours to 9am exceeds 1mm, otherwise 0 |
| 23 | RainTomorrow | Categorical | The amount of next day rain in mm. Used to create response variable RainTomorrow. A kind of measure of the "risk" |

## **Project Notebooks**
The notebooks file of this project can be seen in this [link](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/MLZoomcamp_CapProject.ipynb).  
Objective of this project is to create a rain prediction services to predict the probability whether tomorrow will rain or not (variable y = Yes/No). So in this notebooks, I did some processing before I deploy my model to rain prediction services.
### **Table of Content**
1. Library
2. Dataset
    * Get Dataset
    * Dataset Description
    * Dataset Objectives
    * Dataset Information
    * Features Information
3. Data Preparation
    * Change `Date` feature into DateTime
    * Create new features from `Date` feature (`Day, Month, Year`)
    * Change `Month` feature into Categorical
4. Split Dataset into Train/Val/Test (60%/20%/20%)
5. Exploratory Data Analysis (EDA)
    * Get Numerical and Categorical Features
    * Explore Categorical and Numerical features
    * Check missing value
    * Check outliers in Numerical feature
    * Australia rain season
    * Explore Target (`RainTomorrow`) feature
6. Feature Engineering
    * Deals with missing value
    * Deals with Outliers
7. Feature Importances
    * Mutual Info Score for Categorical features
    * Correlation Matrix and Heatmap for Numerical features
8. Declare Features for Capstone Project
9. OHE with DictVectorizer()
10. Machine Learning Model
    * `LogisticRegression()`
    * `DecisionTreeClassifier()`
    * `RandomForestClassifier()`
    * `XGBoost()`
11. Train the best and final model


## Rain Prediction services codes and tutorial
The codes folder of this project can be seen in this [link](https://github.com/madityarafip/My-Machine-Learning/tree/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes).  
After the final model is obtained, the next process can be carried out:
1. Create [`train.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/train.py) for training the final model, and also save the final model and `DictVectorizer()` into `final_model.bin` using pickle
2. Putting the model into a web service and deploying it locally with `flask`, `pipenv`, and [`Dockerfile`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/Dockerfile)
3. Deploying the subscription services to the cloud with docker container using `flask`, `pipenv`, [`Dockerfile`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/Dockerfile) and [Heroku](https://www.heroku.com)

### Tutorial 1 ?????? Run `train.py` and save the final model and `DictVectorizer()` into `final_model.bin` using pickle
For this part the required file is:
+ [`train.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/train.py)

Steps:
1. Create [`train.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Midterm-Project-Week-7/Mid-Project-Codes/train.py) by exporting the notebook into a python script
2. Open terminal in project folder
3. Run [`train.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/train.py) in terminal using this command:  
   	`python3 train.py`
5. Wait until training process complete
6. And there you have it! The model and `DictVectorizer()` are saved into `final_model.bin`

All of the steps and process can be seen in the video below ??????

https://user-images.githubusercontent.com/42953630/146017997-da277d9e-7d03-4662-8922-cfa387eeb636.mp4


**Note**: 
+ For example of saving and loading the model using `pickle` you can refer to this lesson: [5.2. Saving and loading the model](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/05-deployment/02-pickle.md)

### Test Data
For **Tutorial 2** and **Tutorial 3** we need test data to look at the prediction probabilty of rain generated by the model. For this project I used 4 test data as written below:

1. data_test_1  
```
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
```
2. data_test_2
```
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
```
3. data_test_3
```
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
```
4. data_test_4
```
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
```


### Tutorial 2 ?????? Put model into a web services and deploy it locally with `pipenv` and `Dockerfile`
For this part the required files are:
+ [`predict.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/predict.py)
+ `final_model.bin`
+ `Pipfile` and `Pipfile.lock`
+ `Dockerfile`
+ [`test_local.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/test_local.py)

Steps:
1. Create [`predict.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/predict.py) for load the `final_model.bin` and send the probability prediction result using `flask`
2. Open terminal in project folder and install `pipenv` for python virtual envinronment using this command:  
   		`pip install pipenv`
3. After the `pipenv` installation complete you can install the python libraries that used in this project using this command:  
   		`pipenv install scikit-learn==1.0.0 numpy flask requests gunicorn xgboost`
4. After installing the libraries from process will generate 2 files `Pipfile` and `Pipfile.lock`
5. Create `Dockerfile` with the contents of the script as below  
   ``` 
   FROM python:3.9.7-slim
      
   RUN pip install pipenv

   WORKDIR /app

   COPY ["Pipfile", "Pipfile.lock", "./"]

   RUN pipenv install --system --deploy

   COPY ["predict.py", "final_model.bin", "./"]

   EXPOSE 1208

   ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:1208", "predict:app"] 
   ```
6. Build Docker container using this command:  
   	       `sudo docker build -t cap-pro-mlz .`  
   With -t command we're specifying the tag cap-pro-mlz for this Dockerfile.	       
   You can see this process in this video below ??????
   

https://user-images.githubusercontent.com/42953630/146025178-45b45812-de7f-43c8-accb-1018fa00de30.mp4


7. After the Docker container is build, we can run it, just simply used this command:  
   `sudo docker run -it -p 1208:1208 cap-pro-mlz:latest`  
   Here we use the option -it in order to the Docker run from terminal and shows the result. The -p parameter is used to map the 1208 port of the Docker to 1208 port of our machine. (First 1208 is the Docker container port and the last 1208 is port number for our machine)
8. The docker run rain prediction services and wait for input from test data from [`test_local.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/test_local.py)
9. Run the [`test_local.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/test_local.py) in another terminal (need to open new terminal from project folder) using this command:  
   `pipenv run python test_local.py`
10. Choose test data
11. Wait for the probability prediction process
12. And congratulation! You can get the rain prediction probability for tomorrow and get the suggestion from system whether it will rain tomorrow or not (For this project I give condition it will rain when the probability is >= 60%)

For step 7 - 10 you can see the process in this video below ??????   



https://user-images.githubusercontent.com/42953630/146025703-a88dae95-1a78-4123-80f6-27f68a225746.mp4


**Note**:
+ For tutorial using flask you can refer to this lessons: [5.3. Web services: introduction to Flask](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/05-deployment/03-flask-intro.md) and [5.4. Serving the churn model with Flask](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/05-deployment/04-flask-deployment.md)
+ For example of installing `pipenv` you can refer to this lesson: [5.5. Python virtual environment: Pipenv](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/05-deployment/05-pipenv.md)
+ For example of creating and run Docker container you can refer to this lesson: [5.6. Environment management: Docker](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/05-deployment/06-docker.md)


### Tutorial 3 ?????? Put the web subscription services to the cloud with docker container using Heroku
For this part the required files are:
+ [`predict.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/predict.py)
+ `final_model.bin`
+ `Pipfile` and `Pipfile.lock`
+ [`Dockerfile`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/Dockerfile)
+ [`test_cloud.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/test_cloud.py)

Steps:
1. Create [Heroku](https://www.heroku.com) account
2. Install Heroku CLI
3. Login to Heroku using CLI via terminal using this command:  
   `heroku login`
4. Login to Heroku container registry in terminal using this command:  
   `heroku container:login`
5. Still in the same terminal, create app in Heroku using this command:  
   `heroku create cap-proj-docker`
6. Edit the `Dockerfile`, because heroku can't specify which port we will use, so instead  
   `ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:1208", "predict:app"]`  
   we change that line into
   `ENTRYPOINT ["gunicorn", "predict:app"]`
7. Push docker image to Heroku using this command:  
   `heroku container:push web -a cap-proj-docker`  
   For step 6 and 7 you can see in this video below ??????
   
   
   

https://user-images.githubusercontent.com/42953630/146026397-91baa85d-6d7a-4b21-9287-45278d1d5322.mp4



8. Release the container using this command:  
   `heroku container:release web -a mid-proj-docker`
9. Launch your app to check whether the Docker container is successfully deployed or not (for this project you can click this URL: [https://cap-proj-docker.herokuapp.com/welcome](https://cap-proj-docker.herokuapp.com/welcome))
10. If the Docker container successfully deployed then you can proceed to the next step
11. Open new terminal and run [`test_cloud.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/test_cloud.py) (the different from [`test_local.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Capstone-Project-Week-12/Cap-Projects-Codes/test_local.py) is the desired destination URL, and for this step the URL used is `"http://cap-proj-docker.herokuapp.com/predict"`) 
12. Choose test data
13. Wait for the probability prediction process
14. And congratulation! You can get the rain prediction probability for tomorrow and get the suggestion from system whether it will rain tomorrow or not (For this project I give condition it will rain when the probability is >= 60%)

For step 8 - 14 you can see the process in this video below ??????



https://user-images.githubusercontent.com/42953630/146026858-3b1ad711-de91-46d5-bbd3-62cca976c9f5.mp4


**Note**:
+ For installing and deploying Docker container into Heroku you can refer to this notes by Ninad Date: [How to use Heroku to host your python web app for free](https://github.com/nindate/ml-zoomcamp-exercises/blob/main/how-to-use-heroku.md#deploy-app-docker)


## Navigation
* [ML-Zoomcamp](https://github.com/madityarafip/My-Machine-Learning/tree/main/ML-Zoomcamp)
* Next  -> Week 12 Homework: [Kubernetes and TensorFlow-Serving]()
* Prev. -> Week 9 Homework: [Neural Networks and Deep Learning](https://github.com/madityarafip/My-Machine-Learning/tree/main/ML-Zoomcamp/HW-Week-9)
