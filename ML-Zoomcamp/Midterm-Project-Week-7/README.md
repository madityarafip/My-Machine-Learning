# MIDTERM PROJECT
This project is part of the [Machine Learning Zoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) training held by [DataTalksClub](https://datatalks.club/). In this Midterm Project, everything that has been learned in the previous weeks will be applied in this project. To see what I have learned during this training, you can refer to this following [link](https://github.com/madityarafip/My-Machine-Learning/tree/main/ML-Zoomcamp).  
For this project, similar to what has been studied previously (churning and credit risk), the problem raised in this project is the prediction of whether potential bank clients will subscribe to the term deposit or not ('yes' or 'no' condition).

## About the Dataset
### Data Source
For this project I use the dataset from here: [https://www.kaggle.com/krantiswalke/bankfullcsv](https://www.kaggle.com/krantiswalke/bankfullcsv), or you can also get the dataset from [here](https://raw.githubusercontent.com/madityarafip/My-Machine-Learning/main/Dataset/bank-full.csv).
### Data Description
The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to confirm whether potential bank clients will subscribe to the term deposit or not ('yes' or 'no' condition).
### Features Information
| No. | Feature      | Type | Information     |
| :---: | :---: | :---: | :---: |
| 1   | age   | Numeric   | 0-... |
| 2   | job (Job Type) | Categorical  | admin, bluecollar, entrepreneur, housemaid, management, retired, selfemployed, services, student, technician, unemployed, unknown  |
| 3   | marital (Marital Status)  | Categorical | divorced, married, single, unknown; note: 'divorced' means divorced or widowed |
| 4   |  education | Categorical  | basic.4y, basic.6y, basic.9y, high.school, illiterate, professional.course, university.degree, unknown  |
| 5   |  default (Has credit in default?)  | Categorical   | no, yes, unknown   |
| 6   |  balance (Average yearly balance), in euros  | numeric | 0-...  |
| 7   |  housing (Has housing loan?)   | Categorical   |  no, yes, unknown   |
| 8   |  loan (Has Personal loan?)  |  Categorical  |  no, yes, unknown   |
| 9   |  contact (Contact communication type)  | Categorical   | cellular, telephone |
| 10  |  day (Last contact day of the month)  | Numerical   | 1-31  |
| 11  |  month (Last contact month of year) | Categorical  | jan, feb, mar, apr, may, jun, jul, aug, sep, okt, nov, dec  |
| 12  | duration (Last contact duration)  | Numeric  | Seconds|
| 13  | campaign (Number of contacts performed during this campaign and for this client) | Numeric  | 0-... (Includes last contact) |
| 14  |  pdays (Number of days that passed by after the client was last contacted from a previous campaign) | Numeric  | 0-999 (999 means client was not previously contacted) |
| 15  |  previous (Number of contacts performed before this campaign and for this client) | Numeric | 0-...  |
| 16  |  poutcome (Outcome of the previous marketing campaign) |  Categorical | failure, nonexistent, success |
| 17  |  Target (has the client subscribed a term deposit?) | Categorical  | yes, no |

## Project Notebooks
 
The notebooks file of this project can be seen in this [link](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Midterm-Project-Week-7/MLZoomcamp_MidProject.ipynb).  
Objective of this project is to create a subscription services to predict the probability whether the potential client will subscribe to a term deposit or not (variable y = yes/no). So in this notebooks, I do some processing before I deploy my model to subscription services. The process includes:
1. Data preparation
2. Exploratory data analysis (EDA)  
   What I do in this part: 
    + Check data information
    + Check missing value from the data
    + Change the `'Target'` feature into binary
    + Check if the data is balance or not
    + Look at numerical and categorical features
    + Check unique values in categorical features
    + Visualize numerical features
3. Split dataset ➡️ Train/Val/Test (60%/20%/20%)
4. Features importances  
	 What I do in this part:
	 + View Mutual Info Score for Categorical Features of full train data
	 + Use Correlation Matrix to see correlation between features and target in train data and visualize it using heatmap
5. Choose model  
   The best parameter and model will be selected based on the best performance of the model seen from AUC score of the validation data for each trained model. or this midterm project there are a few model for classification that I used:
   + `LogisticRegression()`
   + `DecisionTreeClassifier()`
   + `RandomForestClassifier()`
   + `XGBoost()`  
   
6. Train the best and final model


## Subscription services codes and tutorial
The codes folder of this project can be seen in this [link](https://github.com/madityarafip/My-Machine-Learning/tree/main/ML-Zoomcamp/Midterm-Project-Week-7/Mid-Project-Codes).  
After the final model is obtained, the next process can be carried out:
1. Create [`train.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Midterm-Project-Week-7/Mid-Project-Codes/train.py) for training the final model, and also save the final model and `DictVectorizer()` into `final_model.bin` using pickle
2. Putting the model into a web service and deploying it locally with `flask`, `pipenv`, and `Dockerfile`
3. Deploying the subscription services to the cloud using `flask` and [PythonAnywhere](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwizz_aRou_zAhUNfX0KHbabAggQFnoECA0QAQ&url=https%3A%2F%2Fwww.pythonanywhere.com%2F&usg=AOvVaw3hzz2q-CdibjXhEo5E-uGB)

### Tutorial 1 ➡️ Run `train.py` and save the final model and `DictVectorizer()` into `final_model.bin` using pickle
For this part the required file is:
+ [`train.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Midterm-Project-Week-7/Mid-Project-Codes/train.py)

### Tutorial 2 ➡️ Put model into a web services and deploy it locally with `pipenv` and `Dockerfile`
For this part the required files are:
+ [`predict.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Midterm-Project-Week-7/Mid-Project-Codes/predict.py)
+ [`test_local.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Midterm-Project-Week-7/Mid-Project-Codes/test_local.py)
+ `Pipfile` and `Pipfile.lock`
+ [`Dockerfile`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Midterm-Project-Week-7/Mid-Project-Codes/Dockerfile)

### Tutorial 3 ➡️ the subscription services to the cloud using PythonAnywhere
For this part the required files are:
+ [`flask_app.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Midterm-Project-Week-7/Mid-Project-Codes/flask_app.py)
+ [`test_cloud.py`](https://github.com/madityarafip/My-Machine-Learning/blob/main/ML-Zoomcamp/Midterm-Project-Week-7/Mid-Project-Codes/test_cloud.py)
