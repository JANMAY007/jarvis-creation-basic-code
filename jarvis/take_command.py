import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init()

#speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#date time
def time():
    Time=datetime.datetime.now().strftime("%I:%M")
    speak(Time)
#time()
def date():
    day=int(datetime.datetime.now().day)
    month=int(datetime.datetime.now().month)
    year=int(datetime.datetime.now().year)
    speak(day)
    speak(month)
    speak(year)
#date()

#Greetings
def wishme():
    speak("Welcome back sir!")
    speak("The current time is")
    time()
    speak("The current date is")
    date()
    Hour=datetime.datetime.now().hour
    if Hour>=6 and Hour<12:
        speak("Good morning Sir!")
        speak("Jarvis your AI assistant is here, how can I help You?")
    elif Hour>=12 and Hour<18:
        speak("Good afternoon Sir!")
        speak("Jarvis your AI assistant is here, how can I help You?")
    elif Hour>=18 and Hour<24:
        speak("Good evening sir!")
        speak("Jarvis your AI assistant is here, how can I help You?")
    else:
        speak("Good night Sir!")
#wishme()

r = sr.Recognizer()
my_mic = sr.Microphone(device_index=1) #my device index is 1, you have to put your device index
#user command
def takeCommand(): 
    r=sr.Recognizer()
    with my_mic as source:
        print("Say now!!!!")
        r.adjust_for_ambient_noise(source) #reduce noise
        audio = r.listen(source) #take voice input from the microphone
    try:
        print("recognizing")
        query=r.recognize_google(audio, language='en-in')
        print(r.recognize_google(audio)) #to print voice into text
    except Exception as e:
        print(e)
        speak("say that again please...")
        return "none"
    return(query)
takeCommand()