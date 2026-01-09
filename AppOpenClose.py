# ********************** Opening and closing Applications **********************

from TextToSpeech import speak
from SpeechToText import listen
from AppOpener import open, close
import pyautogui
import webbrowser


# open Applications
def open_apps(query):
    # if only open in query
    query = query.replace("open", "")
    if not query:
        speak("What should I open")
        open_apps(query=listen())

    # Opening Websites
    elif ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("www.", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")

    # Open google
    elif "google" in query:
        speak("What should I search?")
        while True:
            query = listen()

            if "nothing" in query or "just open" in query:
                webbrowser.open(f"https://www.google.com")
                speak("Opening Google")
                break
            else:
                from SearchOnline import search_google
                search_google(query)
                break

    # Open YouTube
    elif "youtube" in query:
        speak("What should I search?")
        while True:
            query = listen()

            if "nothing" in query or "just open" in query:
                webbrowser.open(f"https://www.youtube.com")
                speak("Opening YouTube")
                break
            else:
                from SearchOnline import search_youtube
                search_youtube(query)
                break

    # Opening closed Tabs in browser
    elif "closed tab" in query:
        speak("Opening the previously closed tabs")
        pyautogui.hotkey("ctrl", "shift", "t")

    # Opening new tabs in browser
    elif "tab" in query:
        speak("Should I search something on new tab?")

        while True:
            query = listen()

            if "no" in query:
                pyautogui.hotkey("ctrl", "t")
                break
            else:
                if "youtube" in query:
                    from SearchOnline import search_youtube
                    search_youtube(query)
                    break
                elif "google" in query:
                    from SearchOnline import search_google
                    search_google(query)
                    break

    # opening installed Apps
    else:
        query = query.replace("launch", "")
        query = query.replace("open", "")
        open(f"{query}", match_closest=True)
        speak(f"Opening {query}")


# Closing Apps
def closing_apps(query):
    # Closing Tabs
    if "tabs" in query:
        speak("How many tabs you want to close")
        while True:
            query = listen()
            if "one" in query or query == 1:
                query = 1
            elif "two" in query or "to" in query or query == 2:
                query = 2
            elif "three" in query or query == 4:
                query = 3
            elif "four" in query or "for" in query or query == 3:
                query = 4
            elif "five" in query or query == 5:
                query = 5
            elif "six" in query or query == 6:
                query = 6
            elif "seven" in query or query == 7:
                query = 7
            elif "eight" in query or "ate" in query or query == 8:
                query = 8
            elif "nine" in query or query == 9:
                query = 9
            elif "ten" in query or query == 10:
                query = 10

            speak("Closing the tabs")
            for i in range(0, query):
                pyautogui.hotkey("ctrl", "w")
            break

    # Closing Current Tab
    elif "tab" in query:
        speak("Closing the current tab")
        pyautogui.hotkey("ctrl", "w")

    # Closing Apps
    else:
        query = query.replace("close the", "")
        query = query.replace("close", "")
        speak(f"Closing {query}")
        close(f"{query}", match_closest=True)
