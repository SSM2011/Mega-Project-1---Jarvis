import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "fc7374cc218d43ce928c686f8dc176fc"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("opening google")
    
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("opening instagram")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("opening youtube")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("opening facebook")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
        speak("Ok Sir")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the JSON response
            data = r.json()

            #Extract the Article
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                speak(article['title'])
    
    else:
        # Let OpenAI handle the request
        pass




if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                
            if word.lower() == "jarvis":
                speak("Yes Sir")
                # Listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                    command = recognizer.recognize_google(audio)
                    processcommand(command)
                    print(command)
                    
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}") 