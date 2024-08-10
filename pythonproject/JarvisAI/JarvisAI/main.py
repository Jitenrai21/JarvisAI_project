import speech_recognition as sr
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    s = input("Enter the word you want to speak it out by computer")
    speaker.Speak(s)
# if __name__ == '__main__':
#     print('pycharm')
#     say("Hello I am Jarvis A.I")