import sys
from SpeechToText import listen

if __name__ == '__main__':
    from GreetMe import greet_me
    greet_me()

    while True:
        query = listen()

        if "open" in query:
            from AppOpenClose import open_apps
            open_apps(query)

        elif "close" in query:
            from AppOpenClose import closing_apps
            closing_apps(query)

        elif "google" in query:
            from SearchOnline import search_google
            search_google(query)

        elif "youtube" in query:
            from SearchOnline import search_youtube
            search_youtube(query)

        elif "wikipedia" in query:
            from SearchOnline import search_wikipedia
            search_wikipedia(query)

        elif "search" in query:
            from SearchOnline import search_about
            search_about(query)

        elif "temperature" in query:
            from aboutNow import temperature_now
            temperature_now(query)

        elif "time" in query:
            from aboutNow import speak_current_time
            speak_current_time(query)

        elif "send" in query and "message" in query:
            from whatsapp import *

        elif "ip address" in query:
            from SearchOnline import get_ip_address
            get_ip_address()

        elif "shutdown the system" in query:
            from SystemControls import shutdown_system, restart_system

            shutdown_system()

        elif "restart the system" in query:
            restart_system()

        elif "bye" in query:
            sys.exit()
