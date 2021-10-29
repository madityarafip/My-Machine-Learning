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

