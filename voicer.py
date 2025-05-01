import os
import sounddevice as sd
import wave
from groq import Groq

# Recording settings
FILENAME = os.path.dirname(__file__) + "/audio.wav"
DURATION = 5  # Record for 5 seconds
SAMPLERATE = 44100

def record_audio():
    print("Recording...")
    audio_data = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype='int16')
    sd.wait()
    print("Recording finished.")
    
    # Save to a WAV file
    with wave.open(FILENAME, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLERATE)
        wf.writeframes(audio_data.tobytes())

def transcribe_audio():
    client = Groq(api_key="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")

    
    with open(FILENAME, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(FILENAME, file.read()),
            model="whisper-large-v3-turbo",
            response_format="verbose_json",
        )
        prompt = transcription.text
        print("Transcription:", prompt)
        return prompt

if __name__ == "__main__":
    record_audio()
    prompt = transcribe_audio()
