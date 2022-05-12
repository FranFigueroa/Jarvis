import pyttsx3
import datetime

engine = pyttsx3.init()
engine.setProperty('voice', 'english_rp+f3')
engine.setProperty('rate',125)
voices = engine.getProperty('voices')
"""engine.setProperty('voice',voices[0].id)"""
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    speak("Friday at your service. How can i help you?")
wishme()
