import pyttsx3
import speech_recognition as sr

from translate import Translator

def takeLanguage():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            try:
                print('Listening')
                r.pause_threshold = 1
                audio = r.listen(source)
                print("Recognizing")
                language = r.recognize_google(audio, language='pl-PL')
                language=language.lower()
                print("output =", language)

                if language == "polski":
                    language = "pl-PL"
                    break
                elif language == "angielski":
                    language = "en-US"
                    break
                else:
                    speak("Zły komunikat, wybierz język polski lub angielski")
            except Exception as e:
                print(e)
                speak("Nie usłyszałem, powtorz jeszcze raz")
               # return "None"
    return language

def takeCommand(language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f'Wprowadz komendę w języku: {language[:2]}')
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, language=language)
            print("Entered:", query)
            return query.lower()

        except Exception as e:
            print(e)
            speak("Powtórz jeszcze raz")
            return "None"
    return query
def translation(text,language):
    if language == "pl-PL":
        translator = Translator(from_lang="pl", to_lang="en")
    elif language == "en-US":
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

        if 'angielski' in query or 'english' in query:
            language = 'en-US'
            speak("Switching to English")
            continue
        elif 'polski' in query or 'polish' in query:
            language = 'pl-PL'
            speak("Zmieniam język na polski")
            continue

        if "bywaj" in query:
            speak("Papaaaa!")
            exit()
        elif "goodbye" in query:
            speak("Bye!")
            exit()

        translated = translation(query, language)
        print(translated)
        if "hello" in translated:
            speak("Hello!")
        else:
            speak(translated)

if __name__ == '__main__':
    Take_query()