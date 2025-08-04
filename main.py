from audio_stream import record_audio
from whisper_transcriber import transcribe_audio
from translator import translate_and_adapt
from voice_generator import speak
from emotion_detector import detect_emotion

def main():
    # 🎙️ Steg 1: Spela in ljud från mikrofonen
    path = record_audio(duration=5)  # inspelning i 5 sekunder

    # 📝 Steg 2: Transkribera ljud till text
    text = transcribe_audio(path)
    print("\n📝 Transkriberad text:")
    print(text)

    emotion = detect_emotion(text, path)
    print(f"\n Upptäckt känsla: {emotion}")


    # 🌍 Steg 3: Översätt + anpassa tonen (formell/informell)
    translated = translate_and_adapt(
        text,
        source_lang="svenska",
        target_lang="engelska",
        tone="formell"  # ändra till "informell" om du vill
    )
    print("\n🌍 Översatt och tonanpassad text:")
    print(translated)

    speak(translated, emotion=emotion)
    
if __name__ == "__main__":
    main()
