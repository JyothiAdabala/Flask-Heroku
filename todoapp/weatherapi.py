import random
import requests
from datetime import datetime


def Greeting():

    res=["Nice to see you. \n",
    "\nIts wonderful to see to you."]
   
    return random.choice(res)


def time_Of_The_Day():
    current_time=datetime.now()
    time_Greeting="Good Morning"
    if current_time.hour>21:
        time_Greeting="Good Night"
    elif current_time.hour>16 and current_time.hour<22:
        time_Greeting="Good Evening"
    elif current_time.hour>=12 and current_time.hour<17:
        time_Greeting="Good Afternoon"
    
    return time_Greeting


def welcome_Greeting():
    
    return f"{time_Of_The_Day()},{Greeting()}"


def evaluator(expression):
  
    try:
        return eval(expression)
    except Exception as e:
        return "Invalid expression"


def weather_report(city_name):

    try:
        data=requests.get("http://api.openweathermap.org/data/2.5/weather?appid=f134f22602331d98954eaf7586ce4265&q={}".format(city_name)).json()
        
    except:
        data={'message':"City Not Found"}
    return data

    