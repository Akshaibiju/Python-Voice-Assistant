# ---- @copyright owner RED TECH WOLF


import pyttsx3
import speech_recognition as sr
import random
import time as t
#!-------------*IMPORTS*--------------!#
import json
from function import bye,hallo,bad_words,dare
from function import morning,evening,night,noon
import webbrowser as wb
import re
from project import data_rem
import pyautogui
import requests	


#!-------------*BASIC DATA*--------------!#
name = "lissy"
id = f"erg9e83509406f {name} MARK1"
password = 1123
version_no = f" {name} automated MARK1 version.no 1.01.1"


#!-------------*greetings*--------------!#
good_morinings = random.choice(morning)
good_evening = random.choice(evening)
good_afternoon = random.choice(noon)
good_night = random.choice(night)
hello = random.choice(hallo)
bye_lissy = random.choice(bye)


#!-------------*RECORDER*--------------!#
def Listener():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("lissy under control .........")
        audio = r.listen(source,0,5)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data.lower()

#!-------------*SPEAK MODULE*--------------!#
def say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('rate',180)
    engine.setProperty('voice', voices[1].id)
    
    print("  ")
    print(f"A.I : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("  ")

#!-------------*BBC NEWS UPDATE*--------------!#
def NewsFromBBC():
	
	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "f48a054d4bda4bf781daba6b18f5542d"
	}
	main_url = " https://newsapi.org/v1/articles"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]

	# empty list which will
	# contain all trending news
	results = []
	
	for ar in article:
		results.append(ar["title"])
		
	for i in range(len(results)):
		
		# printing all trending news
		print(i + 1, results[i])

	#to read the news out loud for us
	from win32com.client import Dispatch
	#speak = Dispatch("SAPI.Spvoice")
	say(results)				

# Driver Code
#if __name__ == '__main__':


#!-------------*RESPONCE MODULE*--------------!#
def lissi(data):
    if "hello" in data.lower():
        say(hello)

    elif "bye" in data.lower():
        say(bye_lissy)
        exit()

    elif "lissy" in data.lower():
        say(hello)

    elif "you can go" in data.lower():
        say("ok boss i am leaving now")
        exit()

    elif "who is" in data.lower():
        say(f"ok boss searching about :  {data}")
        if data.lower() == data.lower():
            #data1 = re.split(' ',data)
            data = data.split(' ')
            search = data[2]
            wikipedia = "https://en.wikipedia.org/wiki/"+ search
            wb.register('chrome', None)
            wb.open(wikipedia)
            True
        if search == ' ' :
            say("cannot recognize mr.akshay boss")

    elif "tell about you" in data.lower():
        say(f"this is {name} id number {id} vertion {version_no}")

    elif "in youtube search about " in data.lower():
        say(f"ok boss searching about : {data}")
        data = data.split(' ')
        search = data[2]
        youtube = "https://www.youtube.com/results?search_query="+search
        wb.register('chrome', None)
        wb.open(youtube)
        True

    elif "are you there" in data.lower():
        say("lissy on duty boss")

    elif "you won it" in data.lower():
        say("THANKYOU BOSS")

    elif "ok you are fast" in data.lower():
        say("you are welcome boss")

    elif "upgrades remaining" in data.lower():
        # YOU CAN ADD ANY REMAINING UPGRADE HERE
        say(data_rem, "these are the taks remaining")

    elif "mark in calender" in data.lower():
        data = data.split(' ')
        duty = data[2]
        with open('project2.txt','w') as f:
            f.write(duty)

    elif "volume down" in data.lower():
        pyautogui.press("volumedown")

    elif "volume up" in data.lower():
        pyautogui.press("volumeup")

    elif "mute" in data.lower():
        pyautogui.press("volumemute")

    elif "news updates" in data.lower():
        say("ok boss")
        NewsFromBBC()

    elif "tell me new update" in data.lower():
        NewsFromBBC()

    elif "give me a dare" in data.lower():
        say("ok boss here is one")
        say(random.choice(dare))
        Listener()
        print(data)
        say("i know that")
        
    #!-------------*greetings*--------------!#
    elif "good morning lissy" in data.lower():
        say(good_morinings)

    elif "good afternoon lissy" in data.lower():
        say(good_afternoon)

    elif "good evening lissy" in data.lower():
        say(good_evening)

    elif "good night lissy" in data.lower():
        say(good_night)

    elif "reset data" in data.lower():
        say("ok boss what do you want me to call you : ")
        Listener()
        data = Listener()
        say(f"ok boss name set to {data}")

    elif "go to web page" in data.lower():
        wb.register('chrome', None)
        wb.open("http://127.0.0.1:5500/fingerprinting.html")
        True

    return data

#!-------------*INITIALIZATION*--------------!#
t.sleep(2)
say("hallo boss")
while 1:
    data = Listener()
    lissi(data)
