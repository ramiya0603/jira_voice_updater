from vosk import Model, KaldiRecognizer
import wave
import json

# Download a Vosk model and extract into ./model
MODEL_PATH = "model"

def transcribe_audio(filename):
    wf = wave.open(filename, "rb")

    model = Model(MODEL_PATH)
    rec = KaldiRecognizer(model, wf.getframerate())

    text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text += " " + result.get("text", "")

    final = json.loads(rec.FinalResult())
    text += " " + final.get("text", "")

    return text.strip()
