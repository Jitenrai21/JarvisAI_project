import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Couldn't understand the message.")
            # sptext()
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id) #[0] indicates male voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    speechtx("Hello I am Jarvis.")
    if 'jarvis' in sptext().lower(): 
        while True:
                data1 = sptext().lower()
                sites = [['youtube', 'https://www.youtube.com/'], ['chat gpt', 'https://chatgpt.com/'], ['github account', 'https://github.com/Jitenrai21']]
                for site in sites:
                    if f'Open {site[0]}'.lower() in data1:
                        speechtx(f'Opening {site[0]}')
                        webbrowser.open(site[1])
                if "how are you" in data1:
                    reply = 'I am doing great, How are you?'
                    speechtx(reply)
                if 'your name' in data1:
                    name = "My name is Javis."
                    speechtx(name)
                elif 'old are you' in data1:
                    age = "I have just been created!"
                    speechtx(age)
                elif "time now" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p") #%I gives hour, %M gives minute, %p gives am pm
                    speechtx(time)
                # elif 'youtube' in data1:
                #     webbrowser.open('https://www.youtube.com/')
                elif 'bargaining' in data1:
                    webbrowser.open('https://www.youtube.com/watch?v=X_e5z_XrlzY&list=PLe9t8KT-SdWXaS4thPTG66mazDoJ2-BJq&index=3')
                elif 'joke' in data1:
                    joke = pyjokes.get_joke(language='en', category='all')
                    print(joke)
                    speechtx(joke)
                elif 'music' in data1:
                    add = r'C:\Users\ACER\OneDrive\Desktop\New folder'
                    list_of_song = os.listdir(add)
                    print(list_of_song)
                    os.startfile(os.path.join(add, list_of_song[0]))
                elif "exit" in data1:
                    speechtx("I am always at your service. Come again.")
                    break    
                # time.sleep(5)
    else:
        print("Call by my name Jarvis for service.")
        speechtx("activate by calling me by my name Jarvis.")
        # sptext()
    