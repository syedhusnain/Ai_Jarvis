import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    voice = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listing........')
        speak('I am listing ....')
        voice.pause_threshold = 3
        audio = voice.listen(source)

        try:
            print('recorginizing....')
            query = voice.recognize_google(audio)
            speak(f'you said {query}')
            print(query)
        except Exception as e:
            print(e)
            print('please Speak Again!')
        return query


def wishyou():
    hours = datetime.datetime.now().hour
    print(hours)
    if hours > 0 and hours < 12:
        speak('Good Morning Husnain Sir')
    elif hours >= 12 and hours < 18:
        speak('Good Afternoon Husnain Sir')
    elif hours >= 18 and hours < 24:
        speak('Good Evening Husnain Sir')
    elif hours == 24:
        speak('Good Night Husnain Sir')
    speak('I am  your A I Assistent .Sir Husnain How may help you.')


if __name__ == '__main__':

    while True:
        query = command().lower()
        if 'hello' in query:
            wishyou()
        elif 'wikipedia' in query:
            query = query.replace('wikipedia', ' ')
            result = wikipedia.summary(query, sentences=2)
            speak('Acording to wikipedia ')
            print(result)
            speak(result)
        elif 'google' in query:
            speak('what you want to search on google. ')
            command = command().lower()
            webbrowser.open(
                f'https://www.google.com/search?source=hp&ei=EWYwXczZOY6jUKu5q8gD&q={command}&oq={command}&gs_l=psy-ab.3..0i67j0j0i10l2j0j0i10l2j0l2j0i10.2081.2971..3923...0.0..0.477.1916.2-4j0j2......0....1..gws-wiz.....0..35i39i70i255j35i39j0i131.rkaP6M4j7uc&ved=0ahUKEwiMpt2LvL7jAhWOERQKHavcCjkQ4dUDCAU&uact=5')
        elif 'youtube' in query:
            speak('what you want to search on youtube ')
            command = command().lower()
            webbrowser.open(f'https://www.youtube.com/results?search_query={command}')
        elif 'play' in query:
            dir='D://Aashiqui 2 2013 (128 kbps)'
            lists=os.listdir(dir)
            os.startfile(os.path.join(dir,lists[0]))

        elif 'time' in query:
            times = datetime.datetime.now().strftime('%H:%M:%S')
            print(times)
            speak(times)
        elif 'laugh'   in query:
            speak('hahahahahhahahahaahah')
        elif 'cry' in query:
            speak('UWaah')
            speak('Uwaah')
            speak('Uwaah')
            speak('Uwaaah')
            speak('uwaah')



        elif 'quite' or 'bey' or 'niklo' in query:
            exit()





