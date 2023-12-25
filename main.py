from fastapi import FastAPI, File, UploadFile
from sr import transcribe_and_translate
import os
from pydub import AudioSegment

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/transcribe_and_translate/")
async def transcribe_and_translate_endpoint(file: UploadFile = File(...), target_language: str = 'es'):
 
    temp_dir = "temp"

  
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    audio_path_mp3 = os.path.join(temp_dir, file.filename)

    audio_path_wav = os.path.join(temp_dir, f"{os.path.splitext(file.filename)[0]}.wav")


    with open(audio_path_mp3, "wb") as buffer:
        buffer.write(file.file.read())

    audio = AudioSegment.from_mp3(audio_path_mp3)
    audio.export(audio_path_wav, format="wav")


    # os.remove(audio_path_mp3)


    result = transcribe_and_translate(audio_path_wav, target_language)

    return {"result": result}