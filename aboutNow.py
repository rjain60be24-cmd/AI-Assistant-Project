# *********************  This Module will give information about what's happening now  ************************

from TextToSpeech import speak
import datetime
import requests
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

def speak_current_time(query):
    # Convert to lowercase for uniform parsing
    query = query.lower()

    # Try to extract place name after "time in" or "time of"
    if "time in" in query:
        place = query.split("time in")[-1].strip()
    elif "time of" in query:
        place = query.split("time of")[-1].strip()
    else:
        place = ""

    # If we have a place, fetch world time
    if place:
        try:
            geolocator = Nominatim(user_agent="time_finder")
            location = geolocator.geocode(place)
            if location:
                tf = TimezoneFinder()
                timezone_str = tf.timezone_at(lng=location.longitude, lat=location.latitude)
                if timezone_str:
                    timezone = pytz.timezone(timezone_str)
                    current_time = datetime.datetime.now(timezone).strftime("%I:%M %p")
                    speak(f"The current time in {place.title()} is {current_time}")
                else:
                    speak(f"Sorry, I couldn't find the timezone for {place.title()}.")
            else:
                speak(f"Sorry, I couldn't locate {place.title()}.")
        except Exception as e:
            speak("Sorry, I couldn't fetch the time due to an error.")
            print(e)
    else:
        # No place provided — use system time
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

def temperature_now(query):
    if "temperature in" in query or "temperature of" in query:
        place = query.split("temperature", 1)[1]
        place = place.replace("in ", "").replace("of ", "").strip()
    else:
        place = "your city"

    # Fetch temperature directly from wttr.in
    url = f"https://wttr.in/{place}?format=%t"
    response = requests.get(url)

    temp = response.text.strip()

    if temp and ("°C" in temp or "+" in temp or "-" in temp):
        speak(f"The temperature in {place} is {temp}")
    else:
        speak("Sorry, I couldn't fetch the temperature right now.")