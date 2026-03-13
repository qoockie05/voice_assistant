from glob import translate

import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
from translate import Translator

def translation(text):
    translator = Translator(to_lang='pl')
    return translator.translate(text)

def takeLanguage():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')

        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")
            language = r.recognize_google(audio, language='pl-in')
            print("output = ", language)

        except Exception as e:
            print(e)
            print("Say that again")
            return "None"
    return language


def takeCommand(language):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')

        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")

            if language == "pl":
                Query = r.recognize_google(audio, language='pl-in')
            if language == "en":
                Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()





def Hello():
    speak("Hejka jestem Ryszard, wybierz język polski lub angielski")


def Take_query():
    Hello()


    while (True):
        query = takeCommand(language).lower()
        if "polski" in query:
            language="pl"
            continue
        elif "angielski" in query:
            language="en"
            continue




        elif "hello" in query:
            speak("Hello!")
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        #exit
        elif "bywaj"  in query:
            speak("Papaaaa!")
            exit()
        elif "goodbye" in query:
            speak("Bye!")
            exit()



if __name__ == '__main__':
    Take_query()