# ********************** Sending message from voice command **********************

from TextToSpeech import speak
from SpeechToText import listen
import pywhatkit
import pyautogui
import time


# Helper function to clean spoken query
def clean_query(text):
    replacements = [
        "send ", "i want ", "to my ", "to ", "my ",
        "i wanna ", "i would like ", "message tu ",
        "message to ", "message "
    ]
    for r in replacements:
        text = text.replace(r, "")
    return text.strip()


# Helper function to check for exit commands
def is_exit_command(text):
    exit_phrases = [
        ("no" in text and "one" in text),
        "come out" in text,
        "come back" in text,
        "exit" in text,
        "i don't want to message" in text,
        "i don't wanna message" in text
    ]
    return any(exit_phrases)


while True:
    speak("Who do you want to message?")

    while True:
        query = listen().lower()
        if query:
            break

    if is_exit_command(query):
        speak("Okay, cancelling the message command. But you can ask me any time if you want to send message to someone in your contacts...")
        break

    name_for_message = clean_query(query)

    if "myself" in name_for_message:
        speak("Are you sure that you want to message yourself?")
    else:
        speak(f"Are you sure you want to message {name_for_message}?")

    while True:
        confirmation = listen()
        if confirmation:
            break

    if "no" in confirmation or "nope" in confirmation or "change" in confirmation:
        continue
    elif is_exit_command(confirmation):
        speak("Okay, cancelling the message command. But you can ask me any time if you want to send message to someone in your contacts...")
        break
    else:
        from getcontact import extract_contacts

        mob_number = extract_contacts(name_for_message)
        not_found_message = f"The name {name_for_message} is not in the contacts."

        if mob_number == not_found_message:
            speak("I can't message someone whose number I don't have.")
            break
        else:
            while True:
                speak("What's the message:")
                message_query = listen()
                if message_query:
                    if "myself" in message_query and "type" in message_query:
                        speak("Type the message:")
                        message = input()
                    else:
                        message = message_query.strip()
                    speak("Are you sure this is the message you want to send?")
                    while True:
                        final_confirmation = listen()
                        if final_confirmation:
                            break

                    if "no" in final_confirmation or "change the message" in final_confirmation:
                        continue
                    else:
                        Maria_msg = f"`{message} ...message by Maria`"
                        speak("Sending the message...")
                        pywhatkit.sendwhatmsg_instantly(f"+91 {mob_number}", Maria_msg)
                        pyautogui.press("enter")
                        time.sleep(2)
                        pyautogui.hotkey("alt", "w")
                        speak("Message sent successfully...")
                        pyautogui.hotkey("alt", "tab")
                        break
            break