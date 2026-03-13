

import pyttsx3
import speech_recognition as sr

from translate import Translator

def takeLanguage():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
        while True:
            try:
                print("Recognizing")
                language = r.recognize_google(audio, language='pl-PL')
                language=language.lower()
                print("output =", language)
            except Exception as e:
                print(e)
                speak("Nie usłyszałem, powtorz jeszcze raz")
                return "None"
            if language == "polski":
                language = "pl-PL"
                break
            elif language == "angielski":
                language = "en-in"
                break
            else:
                speak("Zły komunikat, wybierz język polski lub angielski")
    return language


def takeCommand(language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f'Wprowadz komende w jezyku: {language[:2]}')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")
            if language == "pl-PL":
                Query = r.recognize_google(audio, language='pl-PL')
            elif language == "en-in":
                Query = r.recognize_google(audio, language='en-in')
            print("Entered:", Query)

        except Exception as e:
            print(e)
            print("Say again")
            return "None"

        return Query
def translation(text,language):
    if language == "pl-PL":
        translator = Translator(from_lang="pl", to_lang="en")
    elif language == "en-in":
        translator = Translator(from_lang="en", to_lang="pl")
    else:
        return "Nieobsługiwany język"
    print("Translating...")
    return translator.translate(text)

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def Hello():
    speak("Hejka jestem twoim asystentem glosowym, wybierz język polski lub angielski")


def Take_query():
    Hello()
    language = takeLanguage()
    while (True):
        query = takeCommand(language)
        if query == 'angielski':
            language = 'en-in'
            continue
        elif query == 'polski':
            language = 'pl-PL'
            continue
        translated=translation(query,language)
        print(translated)
        if "hello" in translated:
            speak("Hello!")
        else:
            speak(translated)

        #exit
        if "bywaj"  in query:
            speak("Papaaaa!")
            exit()
        elif "goodbye" in query:
            speak("Bye!")
            exit()

if __name__ == '__main__':
    Take_query()