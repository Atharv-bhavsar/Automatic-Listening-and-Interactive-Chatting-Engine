# File to give ALICE ears

import ai_speak
import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        ai_speak.speak("Listening... waiting for voice input")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            print("Recognizing voice...")
            query = recognizer.recognize_google(audio)
            print("User_Name: ", query)
            return query

        except Exception as e:
            print(e)
            ai_speak.speak("Say that again please...")
            listen()
