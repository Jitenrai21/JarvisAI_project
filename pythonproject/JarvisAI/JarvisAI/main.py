import speech_recognition as sr
import webbrowser
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# while 1:
#     s = input("Enter the word you want to speak it out by computer")
#     speaker.Speak(s)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            speaker.speak("Sorry, I did not catch that. Could you please repeat?")
            return None
        except sr.RequestError as e:
            speaker.speak("Sorry, the speech service is down.")
            print(f"Speech Recognition RequestError: {e}")
            return None
        except Exception as e:
            speaker.speak("An error occurred while processing your request.")
            print(f"Error: {e}")
            return None

if __name__ == '__main__':
    speaker.speak("Hello I am Jarvis AI")
    print("Listening...")
    text = takeCommand()
    speaker.speak(text)
    # while True:
    #     query = takeCommand()
    #
    #     if query is None:
    #         continue
    #
    #     if "open youtube" in query.lower():
    #         speaker.speak("Opening Youtube")
    #         webbrowser.open("https:/www.youtube.com")
