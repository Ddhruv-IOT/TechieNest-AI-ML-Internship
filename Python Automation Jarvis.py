import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from pyfirmata import Arduino,util
from pyfirmata import OUTPUT
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()


board = Arduino('COM4')

board.digital[10].mode = OUTPUT
board.digital[11].mode = OUTPUT
board.digital[12].mode = OUTPUT
board.digital[2].mode = OUTPUT
board.digital[3].mode = OUTPUT
board.digital[4].mode = OUTPUT
board.digital[5].mode = OUTPUT

def multipleled():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(1)

    board.digital[10].write(0)
    board.digital[11].write(1)
    board.digital[12].write(1)

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir")
    
    else:
        speak("Good Evening! Sir")

    speak("I am JARVIS. Please tell me, How may I help you ")
    



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listerning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
     WishMe()
     while True:
        query = takeCommand().lower()

        if'who is' in query:
          speak('searching ')
          multipleled()
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query,sentences=2)
          speak(results)
        

        

        elif'google' in query:
          speak("initiating your request")
          multipleled()
          webbrowser.open(query)
 
        elif'on the motor' in query:
          speak('initiating your request')
          multipleled()
          board.digital[10].write(1)
 
        elif'off the motor' in query:
          multipleled()
          speak('initiating your request')
          board.digital[10].write(0)

        elif'on the tv' in query:
          multipleled()
          speak('initiating your request')
          board.digital[11].write(0)

        elif'tv off' in query:
          multipleled()
          speak('initiating your request')
          board.digital[11].write(1)

        elif'on the fan' in query:

          multipleled()
          speak('initiating your request')
          board.digital[12].write(0)

        elif'off the fan' in query:
          multipleled()
          speak('initiating your request')
          board.digital[12].write(1)
 
        elif 'open water system' in query:
            speak('Yes sir, Opening Water Management System,Todays Water Analytic,  are as follows')
            webbrowser.open("https://thingspeak.com/channels/1376760")
    
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit() 