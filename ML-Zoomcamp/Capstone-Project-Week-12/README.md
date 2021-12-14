# **CAPSTONE PROJECT: RAIN PREDICTION IN AUSTRALIA**
This project is part of the [Machine Learning Zoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) training held by [DataTalksClub](https://datatalks.club/). In this Midterm Project, everything that has been learned in the previous weeks was applied in this project. To see what I have learned during this training, you can refer to this following [link](https://github.com/madityarafip/My-Machine-Learning/tree/main/ML-Zoomcamp). The problem raised in this project is the prediction of whether tomorrow will rain or not based from Australia weather dataset. ('Yes' or 'No' condition).


## **Project Notebooks**
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
