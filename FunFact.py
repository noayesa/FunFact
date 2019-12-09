# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:23:28 2019

@author: Noa
"""
import requests
import smtplib
from pandas.io.json import json_normalize
import xml.etree.ElementTree as ET



def catFact(): #get json format
    response = requests.get('https://catfact.ninja/fact?max_length=140')
    text = json_normalize(response.json())
    funFact = (text.fact)

    return funFact[0]
    

def dailyFact(): #get xml format
    response = requests.get("http://www.fayd.org/api/fact.xml")
    root = ET.fromstring(response.content) 

    return root[1].text #the nested fact
    
    

def sendEmail():
    
    #Connecting to server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.ehlo()
    s.login('EMAIL@gmail.com', 'PASSWORD') #User's email
    
    message = "Subject: Fun Fact \n\n{}".format(dailyFact())
    
     #email address of the user. List of email addresses you want to send to
    s.sendmail('sender\'s email', ['email address1','email address2'] , message)
    s.close()

def sendCatEmail():
    
    #Connecting to server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.ehlo()
    s.login('EMAIL@gmail.com', 'PASSWORD') #User's email
    
    message = "Subject: Cat Fact \n\n{}".format(catFact())
    
    #email address of the user. List of email addresses you want to send to
    s.sendmail('sender\'s email', ['email address1','email address2'] , message)
    s.close()
    



sendEmail()
sendCatEmail()

