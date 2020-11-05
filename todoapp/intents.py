name=" "
from .weatherapi import *
def get_intent(data):
    global name
    m=data['message'].lower()
    if data['key']=='name':
        name=m
        return 'next'
    if data['key']=='City Name':
        return 'weatherresult'
    if data['key']=='expression':
        return 'expressionres'
    

    if any(x in m for x in ["calculation","evaluate","calculate","calculations"]):
        return "expression"
    elif "weather" in m:
        return "City Name"
    elif "fetch" in m:
        return "fetch"
    else:
        return "echo"


def handle(data):
    global name
    from flask import render_template
    intent=get_intent(data)

    if intent == 'next':
         return render_template('messages/greet.html',data={'greet':welcome_Greeting()},name=name,question={'key':'Choice','text':'What would you like me to do'})
    elif intent == 'City Name':
        return render_template('messages/botmsgs.html', name=name,question={'key':'City Name','text':'Enter city name'})
    elif intent =='weatherresult':
         return render_template('messages/weatherres.html',data=weather_report(data['message']),name=name,question={'key':'Choice','text':'What would you like me to do'})
    elif intent =='expression':
        return render_template('messages/botmsgs.html', name=name,question={'key':'expression','text':'Enter your expression'})
    elif intent =='expressionres':
        return render_template('messages/calculation.html',data=evaluator(data['message']),name=name,question={'key':'Choice','text':'What would you like me to do'})
    else:
        return render_template('messages/botmsgs.html',name=name,question={'key':'Choice','text':'Something went wrong'})