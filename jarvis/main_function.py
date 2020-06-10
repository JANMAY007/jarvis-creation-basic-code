import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui as pg
import psutil._psutil_windows
import pyjokes
import smtplib
import socket
import pyaudio

engine=pyttsx3.init()

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#date time
def time():
    Time=datetime.datetime.now().strftime("%I:%M")
    speak("The current time is")
    speak(Time)

def date():
    day=int(datetime.datetime.now().day)
    month=int(datetime.datetime.now().month)
    year=int(datetime.datetime.now().year)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)


#Greetings
def wishme():
    speak("Welcome back sir!")
    Hour=datetime.datetime.now().hour
    if Hour>=6 and Hour<12:
        speak("Good morning Sir! Hope you are have a nice day!")
        speak("Baburao your AI assistant is here, how can I help You?")

    elif Hour>=12 and Hour<18:
        speak("Good afternoon Sir! Hope you are having a nice day!")
        speak("Baburao your AI assistant is here, how can I help You?")

    elif Hour>=18 and Hour<24:
        speak("Good evening sir!  Hope you are having a nice day!")
        speak("Sir please sleep early.")
        speak("Baburao your AI assistant is here, how can I help You?")

    elif 'do you remember anything' in query:
        remember=open('data.txt','r')
        speak("you said me to remember that "+remember.read())

    else:
        speak("Good night Sir! Hope you are had a nice day!")


r = sr.Recognizer()
my_mic = sr.Microphone(device_index=1) #my device index is 1, you have to put your device index
#user command
def takeCommand():
    r=sr.Recognizer()
    with my_mic as source:
        speak("Whats my next task?")
        r.adjust_for_ambient_noise(source) #reduce noise
        audio = r.listen(source) #take voice input from the microphone

    try:
        speak("recognizing your command!")
        query=r.recognize_google(audio, language='en-in')
        print(r.recognize_google(audio)) #to print voice into text
    except Exception as e:
        print(e)
        speak("I did not get it, say that again please...")
        return "none"
    return(query)


#send email
def sendEmail(to,content):
    speak("what should i say?")
    message=takeCommand()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.connect("smtp.gmail.com",465)
    server.ehlo()
    server.starttls()
    server.ehlo()
    smtpObj = smtplib.SMTP('localhost')
    reciever='emailid'
    sender='emailid'
    server.login("emailid", "password")
    smtpObj.sendmail(sender, reciever, message)
    speak("email was succesfully sent.")


#screenshot
def screenshot():
    img=pg.screenshot()
    img.save("my_screenshot.png")



#cpu usage
def cpu():
    usage=str(psutil.cpu_percent())
    speak("The cpu usage is "+usage)


#battery usage
def battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    speak(percent)


#jokes
def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                sendEmail()
            except Exception as e:
                print(e)
                speak("unable to send email.")

        elif 'chrome' in query:
            speak("what should i search?")
            chromepath='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            search=takeCommand().lower()
            try:
                wb.register('chromex', None, wb.BackgroundBrowser(chromepath))
                wb.get('chromex')
                wb.open_new(search)
            except:
                wb.open_new(search)

        elif 'remember that' in query:
            speak("what should i remember?")
            data=takeCommand()
            speak("you said me to remember that "+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'screenshot' in query:
            screenshot()
            speak("Done! Your screenshot saved.")

        elif 'cpu usage' in query:
            cpu()

        elif 'battery' in query:
            battery()

        elif 'joke' in query:
            jokes()

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'offline' in query:
            speak("Going offline")
            quit()
