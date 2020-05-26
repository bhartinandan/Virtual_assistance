import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishes():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("Hello I am bucchi what can i help you")


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

   

if __name__ == "__main__":
    speak('welcome to the bucchi world')
    while True:
        z = sr.Recognizer()
        with sr.Microphone()as source:
            z.pause_threshold = 1
            audio = z.listen(source)
            order = z.recognize_google(audio, language='en-in')
            print(order)
            if'wake up' in order:
                wishes()
                while True:
                    query = takecommand().lower()
                    if 'wikipedia' in query:
                        speak('searching wikipedia...')
                        query = query.replace("wikipedia","_")
                        results = wikipedia.summary(query, sentences=2)
                        speak("according to wikipedia")
                        speak(results)
                    elif 'open youtube' in query:
                        speak('please wait opening youtube in web browser')
                        webbrowser.open("youtube.com")
                        
                    elif'youtube in chrome' in query:
                        speak('please wait opening youtube in chrome')
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open('https://www.youtube.com/')

                    elif'open chrome' in query:
                        speak('please wait opening chrome')
                        path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                        os.startfile(path)

                    elif'open whatsapp' in query:
                        speak('please wait opening whatsapp in chrome')
                        path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                        webbrowser.get(path).open('https://web.whatsapp.com/')

                    elif'open pycharm' in query:
                        speak('please wait opening pycharm')
                        path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe"
                        os.startfile(path)

                    elif'open zoom' in query:
                        speak('please wait opening zoom')
                        path = "C:\\Users\\shaur\\OneDrive\\Desktop\\ZoomInstaller.exe"
                        os.startfile(path)

                    elif'who are you'in query:
                        speak('myself bucchi i am a virtual assistance work on voice commands designed for helping you by my master named bharti nandan')

                    elif'open linkedin' in query:
                        speak('please wait opening linkedin in chrome')
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open('https://www.linkedin.com/')

                    elif'open udemy' in query:
                        speak('please wait opening udemy')
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open('https://www.udemy.com/')

                    elif'open hackerrank' in query:
                        speak("please wait opening hacker rank")
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open('https://www.hackerrank.com/')

                    elif'sleep' in query:
                        speak('thank you master i am going to sleep')
                        break
                    else:
                        speak('sorry your given command is not defined please give some defined command')
            else:
                continue
                
