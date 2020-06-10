import pyttsx3
import datetime

engine = pyttsx3.init()

#convert to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#date time
def time():
    Time=datetime.datetime.now().strftime("%I:%M")
    speak(Time)
time()
def date():
    day=int(datetime.datetime.now().day)
    month=int(datetime.datetime.now().month)
    year=int(datetime.datetime.now().year)
    speak(day)
    speak(month)
    speak(year)
date()