#Questionaire 

#Hours = On average, how many hours of sleep do you get on a weeknight?

#PhoneReach = Do you sleep with your phone within arms reach?

#PhoneTime = Do you use your phone within 30 minutes of falling asleep?

#Tired = On a scale from 1 to 5, how tired are you throughout the day? (1 being not tired, 5 being very tired)

#Breakfast = Do you typically eat breakfast?

import pandas as pd
import numpy as np 
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv (r'SleepStudyData.csv')
#
print(df.head())

df['PhoneReach'] = df['PhoneReach'].map(
                   {'Yes':True ,'No':False})
df['PhoneTime'] = df['PhoneTime'].map(
                   {'Yes':True ,'No':False})
df['Breakfast'] = df['Breakfast'].map(
                   {'Yes':True ,'No':False})


df.fillna(method ='ffill', inplace = True)

X = np.array(df[['Hours','PhoneReach','PhoneTime','Breakfast']])
Y = np.array([df['Tired']])

df.dropna(inplace = True)

X, X_test, Y, Y_test = train_test_split(X, Y)

linear_regression = LinearRegression()
linear_regression.fit(X,Y)
score = linear_regression.predict([[1.0,True,True,True]])
def ask_user():
    hours_slept = float(input("On average, how many hours of sleep do you get on a weeknight?"))
    Phone_Reach = eval(input("you sleep with your phone within arms reach (True/False)?"))
    Phone_time =  eval(input("you use your phone within 30 minutes of falling asleep? (True/False)?"))
    Breakfast   = eval(input("You typically eat breakfast? (True/False)"))
    score = linear_regression.predict([[hours_slept,Phone_Reach,Phone_time,Breakfast]])
    sleep_index = 10-(score*2)
    print(f"Your sleep score is {sleep_index} out of 10")
          
ask_user()