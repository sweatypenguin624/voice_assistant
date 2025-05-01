import os
import sounddevice as sd
import wave
from groq import Groq
from kokoro import KPipeline
import soundfile as sf
import numpy as np
import datetime
import requests
import time

# Recording settings
FILENAME = os.path.dirname(__file__) + "/audio.wav"
DURATION = 5  # Record for 5 seconds
SAMPLERATE = 44100

def record_audio():
    print("Recording...")
    audio_data = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype='int16')
    sd.wait()
    print("Recording finished.")
    
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

def get_current_datetime():
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d, %Y %I:%M %p")

def get_weather():
    return ("For Saturday, March 22, 2025, in Bengaluru, India, the weather forecast is as follows:\n"
            "• Temperature: High around 33.3°C (91°F) and low around 22.1°C (72°F).\n"
            "• Precipitation: There is an 84% chance of precipitation, indicating a possibility of patchy rain in nearby areas.\n"
            "• Conditions: The day is expected to start with partly cloudy skies, transitioning to light rain later.")

if __name__ == "__main__":
    record_audio()
    user_input = transcribe_audio().lower()
    
    if "time" in user_input or "date" in user_input:
        assistant_response = get_current_datetime()
    elif "weather" in user_input:
        assistant_response = get_weather()
    # elif " MET university " in user_input:
    #     assistant_response = ("Amity University Bengaluru is a branch of Amity University, offering quality education "
    #                           "in a modern and vibrant environment. Located in Karnataka’s tech hub, the university "
    #                           "provides undergraduate, postgraduate, and doctoral programs in engineering, management, "
    #                           "law, science, and more. It emphasizes research, innovation, and industry collaborations, "
    #                           "preparing students for global careers. The campus is equipped with advanced infrastructure, "
    #                           "experienced faculty, and state-of-the-art labs. Amity Bengaluru also focuses on placements, "
    #                           "entrepreneurship, and extracurricular activities, ensuring holistic development. Recognized "
    #                           "by UGC and other regulatory bodies, it is a preferred choice for students seeking a "
    #                           "world-class education in Bengaluru.")
    else:
        client = Groq(api_key="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")
        completion = client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.6,
            max_completion_tokens=4096,
            top_p=0.95,
            stream=True,
            stop=None,
        )
        assistant_response = ""
        print("Assistant:", end=" ")
        for chunk in completion:
            text_chunk = chunk.choices[0].delta.content or ""
            print(text_chunk, end="")
            assistant_response += text_chunk
        print()
    
    pipeline = KPipeline(lang_code='a')
    generator = pipeline(assistant_response, voice='af_heart', speed=1, split_pattern=None)
    full_audio = []
    
    for i, (gs, ps, audio) in enumerate(generator):
        print(i, gs, ps)
        full_audio.append(audio)
    
    final_audio = np.concatenate(full_audio)
    sf.write('full_output.wav', final_audio, 24000)
    
    # Wait for the file to be fully written before playing
    time.sleep(1)
    print("Playing generated audio...")
    os.system("start full_output.wav" if os.name == "nt" else "afplay full_output.wav" if os.name == "posix" else "aplay full_output.wav")