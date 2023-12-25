import speech_recognition as sr
from googletrans import Translator

def transcribe_and_translate(audio_path, target_language='en'):
    recognizer = sr.Recognizer()
    translator = Translator()

    audio_file = sr.AudioFile(audio_path)
    with audio_file as source:
        audio_data = recognizer.record(source)
    print("Recognizing...", audio_file, audio_data)
    try:
        text = recognizer.recognize_google(audio_data, language='es')
        translated_text = translator.translate(text, dest=target_language).text
        return translated_text
    except sr.UnknownValueError:
        return "No se pudo entender el audio"
    except sr.RequestError as e:
        return f"Error en la solicitud al servicio de reconocimiento de voz: {e}"
    

