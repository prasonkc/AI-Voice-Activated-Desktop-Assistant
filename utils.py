import speech_recognition as sr
import os
import pyttsx3


def speak(inp):
    print("Ai :" + inp)
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[3].id)  # set 1
    engine.say(inp)
    engine.runAndWait()


def listen():
    # rec = sr.Recognizer()
    # mic = sr.Microphone(device_index=1)  # my device index is 1, you have to put your device index

    # try:
    #     with mic as source:
    #         print("Listening...")
    #         rec.adjust_for_ambient_noise(source)  # reduce noise
    #         audio = rec.listen(source)
    #         text = rec.recognize_google(audio)  # take voice input from the microphone
    #     return text
    return input("command: ")

    # except sr.UnknownValueError:
    #     print("Sorry, I couldn't understand.")
    # except sr.RequestError as e:
    #     print("Sorry, an error occurred while recognizing speech:", str(e))


