import datetime
from Speak import say
import wikipedia
import pywhatkit  # It supports google search

def time():
    time = datetime.datetime.now().strftime("%H:%M")
    say(time)

def date():
    date = datetime.date.today()
    say(date)

def day():
    day = datetime.datetime.now().strftime("%A")
    say(day)

def non_input_execution(query):
    queery = str(query)
    if "time" in query:
        time()
    elif "date" in query:
        date()
    elif "day" in query:
        day()   

def input_execution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("what is", "").replace("about", "").replace("who is", "").replace("wikipedia", "")
        result = wikipedia.summary(name)
        say(result) 
    elif "google" in tag:
        query = str(query).replace("google", "")
        query = str(query).replace("search", "")
        pywhatkit.search(query)
