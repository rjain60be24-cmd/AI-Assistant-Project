import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  # Get available voices
    engine.setProperty('voice', voices[1].id)  # Set voice by index
    print(f'Maria: {text}')
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    # Example usage
    speak("Hello! This is voice number zero.")




    