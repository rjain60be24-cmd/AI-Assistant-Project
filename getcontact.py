from TextToSpeech import speak
from SpeechToText import listen
import pandas as pd

def extract_contacts(name_for_message):
    # Load the CSV file
    df = pd.read_csv('my_contacts.csv')

    # Convert the 'Name' column to lower case for case-insensitive search
    df['Name_lower'] = df['Name'].str.lower()

    # User inputs the name
    name = name_for_message

    # Find the rows that contain the name
    rows = df[df['Name_lower'].str.contains(name)]

    # If there's more than one match, ask the user for more details

    if len(rows) > 1:
        speak("Multiple contacts found:")
        for i, row in rows.iterrows():
            print(row['Name'])
        speak("Please tell more details: ")

        while True:
            more_details = listen()
            if not more_details:
                continue
            else:
                break

        # Search within the previously matched names
        rows = rows[rows['Name_lower'].str.contains(more_details)]
    elif len(rows) == 0:
        # If no match is found, print a message and return
        speak(f"The name {name} is not in the contacts.")
        mob_number = f"The name {name} is not in the contacts."
        return mob_number

    mob_number = rows['Phone Number'].values[0]

    # Print the full name and phone number in the desired format
    return mob_number