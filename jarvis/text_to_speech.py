import pyttsx3

#text to speech
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

you_speak=input()
speak(you_speak)