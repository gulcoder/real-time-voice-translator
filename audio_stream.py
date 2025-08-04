import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(filename="input.wav", duration=5, fs=44100):
    print("🎙️ Spelar in...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    os.makedirs("audio", exist_ok=True)
    path = os.path.join("audio", filename)
    write(path, fs, recording)
    print("✅ Inspelning klar.")
    return path
