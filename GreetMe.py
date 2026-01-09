# *********************  greeting in starting  ************************

from datetime import datetime
from TextToSpeech import speak

# greet me function
def greet_me():
    hour = int(datetime.now().hour)

    if 0 <= hour <= 12:
        greet = "Good Morning"
    elif 12 < hour < 18:
        greet = "Good Afternoon"
    else:
        greet = "Good Evening"

    speak(f"{greet}!, I am your personal assistant, Please tell me how can i help...")

if __name__=="__main__":
    greet_me()