import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

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
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id) #[0] indicates male voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    # if sptext().lower() == 'jarvis':
        data1 = sptext().lower()
        if 'your name' in data1:
            name = "My name is Javis."
            speechtx(name)
        elif 'old are you' in data1:
             age = "I have just been created!"
             speechtx(age)
    # else:
        # print("Call me by name Jarvis to get tasks executed!")
