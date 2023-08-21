import pyttsx3

def say(text):
    engine = pyttsx3.init("sapi5")  # sapi5 is a  Speech Application Programming Interface or SAPI is an API developed by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications.
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 170)  # It's like speed of the voice.
    print("   ")
    print(f"Leon: {text}")
    engine.say(text)
    engine.runAndWait()
    print("   ")







