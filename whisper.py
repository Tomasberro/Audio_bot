# import openai
# import os
# import base64

# openai.api_key = os.environ.get("OPENAI_API_KEY")

# audio_path = 'temp/WhatsApp Ptt 2023-12-23 at 10.36.07.wav'


# with open(audio_path, 'rb') as audio_file:
#     audio_base64 = base64.b64encode(audio_file.read()).decode('utf-8')


# response = openai.Whisper.transcribe(audio=audio_base64, language="es")

# transcription = response['transcriptions'][0]['text']
# print("Transcripción:", transcription)
