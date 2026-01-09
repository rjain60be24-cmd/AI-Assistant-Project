# ************** This module is used to search anything from Google, youtube, wikipedia **************

import random
import webbrowser
from requests import get
import pywhatkit
import wikipedia
from TextToSpeech import speak
from SpeechToText import listen

# search on Google
def search_google(query):
    import wikipedia as google_scrap
    query = query.replace("open google and search", "")
    query = query.replace("search about", "")
    query = query.replace("search", "")
    query = query.replace(" on google", "")
    query = query.replace("google", "")
    query = query.replace("find about", "")
    query = query.replace("find", "")

    speak("This is what I found")
    try:
        pywhatkit.search(query)
        result = google_scrap.summary(query, 1)
        speak(result)
    except ValueError:
        speak("There is no TTS.speakable output...")


# search on YouTube
def search_youtube(query):
    query = query.replace("search about", "")
    query = query.replace("search", "")
    query = query.replace("find", "")
    query = query.replace("from youtube", "")
    query = query.replace("on youtube", "")
    confirmation = query
    query = query.replace("play", "")
    what = query
    web = "https://www.youtube.com/results?search_query=" + query
    if "play" in confirmation:
        if "music" in what:
            speak("playing your liked music")
            x = (1, 2, 3, 4)
            y = random.choice(x)
            if y == 1:
                webbrowser.open("https://www.youtube.com/watch?v=QF8zQxLBii4&list=RDQF8zQxLBii4&start_radio=1")
            elif y == 2:
                webbrowser.open("https://www.youtube.com/watch?v=S1u01VnB4Vc&list=RDS1u01VnB4Vc&start_radio=1")
            elif y == 3:
                webbrowser.open("https://www.youtube.com/watch?v=88T3-yxh2P8&list=RD88T3-yxh2P8&start_radio=1")
            elif y == 4:
                webbrowser.open("https://www.youtube.com/watch?v=WZjqblzUIXE&list=RDWZjqblzUIXE&start_radio=1")
        else:
            speak("This is what I found for your search!")
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Done")
    else:
        speak("May I play the best result for you")
        webbrowser.open(web)
        confirmation = listen()
        if "no" in confirmation or "nope" in confirmation or "na" in confirmation or "don't" in confirmation:
            speak("Done")
        else:
            pywhatkit.playonyt(query)
            speak("Done")


# Search on Wikipedia
def search_wikipedia(query):
    speak("Searching from wikipedia....")
    query = query.replace("on wikipedia", "")
    query = query.replace("search about", "")
    query = query.replace("search", "")
    query = query.replace("find", "")
    query = query.replace("wikipedia", "")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia..")
        speak(results)
    except ValueError:
        speak("Sorry, Nothing Found on wikipedia")


# search about
def search_about(query):
    query = query.replace("search about", "")
    query = query.replace("search", "")
    query = query.replace("find about", "")
    query = query.replace("find", "")
    if not query:
        speak("What should i do")
        while True:
            query = listen()
            if "google" in query or "temperature" in query:
                search_google(query)
                break
            elif "youtube" in query:
                search_youtube(query)
                break
            elif "wikipedia" in query:
                search_wikipedia(query)
                break
            else:
                break
    else:
        speak("Where should i search")
        while True:
            where_query = listen()
            if "google" in where_query:
                search_google(query)
                break
            elif "youtube" in where_query:
                search_youtube(query)
                break
            elif "wikipedia" in where_query:
                search_wikipedia(query)
                break


# IP Address
def get_ip_address():
    ip = get('https://api.ipify.org').text
    speak(f"your IP address is {ip}")
