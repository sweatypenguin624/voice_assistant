from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import numpy as np  # Added for merging audio files

pipeline = KPipeline(lang_code='a')

text="Helloo! How are you doing today?"
generator = pipeline(text, voice='af_heart', speed=1, split_pattern=None)  # Prevents automatic splitting

full_audio = []
for i, (gs, ps, audio) in enumerate(generator):
    print(i)
    print(gs)
    print(ps)
    full_audio.append(audio)  # Collect all audio chunks

final_audio = np.concatenate(full_audio)  # Merge all chunks into one
display(Audio(data=final_audio, rate=24000, autoplay=True))  # Play final audio
sf.write('full_output.wav', final_audio, 24000)  # Save as a single file
