# File to translate from any language to English using ALICE

# Import required modules
import ai_speak
import googletrans


def translate(query):
    # Displaying message
    print("Translating text")
    ai_speak.speak("Translating text")

    # Creating translator object
    translator = googletrans.Translator()

    # Translating text to English
    translated_text = translator.translate(query, dest="en")
    return translated_text.text
