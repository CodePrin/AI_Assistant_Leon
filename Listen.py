import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 10) # This means that after 5 seconds it will start recognizing it.

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"You said: {query}")

    except:
        return ""
    
    query = str(query)
    return query.lower()



