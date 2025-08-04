#import pyttsx3

#def speak(text):
    #engine = pyttsx3.init()
    #engine.setProperty('rate', 160)  # justera hastighet
    #engine.setProperty('volume', 1.0)
    #engine.say(text)
    #engine.runAndWait()

import pyttsx3

def speak(text, emotion="neutral"):
    engine = pyttsx3.init()

    if emotion == "happy":
        engine.setProperty('rate', 200)   # snabbare tal
        engine.setProperty('volume', 1.0) # högre volym (max 1.0 dock)
    elif emotion == "angry":
        engine.setProperty('rate', 140)   # lite långsammare
        engine.setProperty('volume', 1.0)
    else:
        engine.setProperty('rate', 160)
        engine.setProperty('volume', 1.0)

    print(f"Läser upp med ton: {emotion}")
    engine.say(text)
    engine.runAndWait()
