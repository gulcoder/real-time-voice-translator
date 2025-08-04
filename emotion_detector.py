import librosa
import numpy as np

def detect_emotion_from_audio(path):
    y, sr = librosa.load(path)
    energy = np.mean(librosa.feature.rms(y=y))
    pitch, _ = librosa.piptrack(y=y, sr=sr)
    mean_pitch = np.mean(pitch[pitch > 0])

    print(f"Pitch: {mean_pitch:.1f}, Energi: {energy:.4f}")

    if mean_pitch > 200 and energy > 0.05:
        return "happy"
    elif mean_pitch < 150 and energy < 0.04:
        return "angry"
    else:
        return "neutral"

def detect_emotion_from_text(text):
    text = text.lower()
    if any(word in text for word in ["förbannad", "jävla", "skit", "fan", "arg", "jättearg", "ilsken"]):
        return "angry"
    elif any(word in text for word in ["glad", "kul", "toppen", "fantastiskt", "härligt", "underbart", "jättekul"]):
        return "happy"
    else:
        return "neutral"

def detect_emotion(text, audio_path):
    from_audio = detect_emotion_from_audio(audio_path)
    from_text = detect_emotion_from_text(text)

    if from_audio == from_text:
        return from_audio
    
    if from_text in ["angry", "happy"] and from_audio=="neutral":
        return from_text
    
    return from_audio