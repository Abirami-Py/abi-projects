import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import speech_recognition as sr
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')

if len(voices)>1:
    engine.setProperty('voices',voices[1].id)
else:
    engine.setProperty('voices',voices[0].id)

def engine_talk(text):
    print(f"Alexa is Saying :{text}")
    engine.say(text)
    engine.runAndWait()

def user_commands():
    try:
        with sr.Microphone()as source:
            listener.adjust_for_ambient_noise(source)
            print("Start speeking !!")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            if 'alexa' in command:
                command=command.replace("alexa","")
                print(f"User Said: {command}")
                return command
    except Exception as e:
        print(f"Error :{e}")
        return ""

def run_alexa():
    command=user_commands()
    if command:
        if 'play' in command:
            song=command.replace('play','')
            engine_talk("playing"+song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time=datetime.now().srtftime('%I:%M:%p')
            engine_talk('the current time is'+time)
        elif 'who is' in command:
            name=command.replace('who is ','')
            info=wikipedia.summary(name,l)
            print(info)
            engine_talk(info)
        elif'joke' in command:
            engine_talk(pyjokes.get_joke())
        elif 'stop' in command:
            sys.exit()
        else:
            print("i could not hear you properly")
    else:
        engine_talk(" I did not catch that . please speak again")    

while True:
    run_alexa()








