# ***************** This module will control your System controls *****************

import os
from TextToSpeech import speak

# shutdown the System
def shutdown_system():
    speak("Good Bye...")
    os.system("shutdown /s /t 5")


# Restart the System
def restart_system():
    speak("I am restarting the system.. Don't forget to run my code again to awake me")
    os.system("shutdown /r /t 5")
