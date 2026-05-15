import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests


newsApi = '804f467902a043dca3ff241d0ab82135'

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
    except sr.WaitTimeoutError:
        return ""

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        print("Say 'Hello' to activate...")
        word = listen()

        if "hello" in word:
            speak("Yes Boss, how can I help you?")

        elif "youtube" in word:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "facebook" in word:
            speak("Opening Facebook")
            webbrowser.open("https://facebook.com")

        elif "linkdin" in word:
            speak("Opening linkdin")
            webbrowser.open("https://linkdin.com")

        elif "stop" in word:
            speak("Goodbye!")
            break
        elif word.lower().startswith("play"):
            song = word.lower().split("")[1]
            link = music_library.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")
        elif "news" in word:
            url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsApi}"
            r = requests.get(url)
            data = r.json()
            articles = data["articles"][:5]
            for article in articles:
                speak(article["title"])
