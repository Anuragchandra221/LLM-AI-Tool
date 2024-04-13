import speech_recognition as sr
from googletrans import Translator

def recognize_and_translate_malayalam(audio_file_path):
    
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    malayalam_text = recognizer.recognize_google(audio_data, language="ml-IN")

    
    translator = Translator(to_lang="en", from_lang="ml")
    translated_text = translator.translate(malayalam_text)

    return translated_text

translated_text = recognize_and_translate_malayalam("C:/Users/hp/Desktop/LLM-AI-Tool/audi.wav")
print("Translated Text:", translated_text)