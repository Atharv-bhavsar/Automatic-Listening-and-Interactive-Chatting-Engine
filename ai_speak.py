# File to give ALICE voice

import pyttsx3

voice_engine = pyttsx3.init("sapi5")

# rate = voice_engine.getProperty("rate")
# print (rate)
voice_engine.setProperty("rate", 150)

# volume = voice_engine.getProperty("volume")
# print(volume)
voice_engine.setProperty("volume", 1)

voice = voice_engine.getProperty("voices")
voice_engine.setProperty("voice", voice[1].id)


def speak(audio):
    voice_engine.say(audio)
    voice_engine.runAndWait()
