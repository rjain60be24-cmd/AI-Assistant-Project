import pandas as pd

# Load the CSV
contacts = pd.read_csv("contacts.csv")

# Clean column names (remove leading/trailing spaces)
contacts.columns = contacts.columns.str.strip()

# Create a full name by joining first, middle, and last names
contacts['Full Name'] = contacts[['First Name', 'Middle Name', 'Last Name']].fillna(' ').agg(''.join, axis=1).str.strip()

# Take only 'Full Name' and 'Phone 1 - Value'
new_data = contacts[['Full Name', 'Phone 1 - Value']].copy()

# Clean the phone numbers
new_data['Phone 1 - Value'] = new_data['Phone 1 - Value'].astype(str) \
    .str.replace('+91', '', regex=False) \
    .str.replace(' ', '') \
    .str.strip()

# Rename the columns properly
new_data = new_data.rename(columns={
    'Full Name': 'Name',
    'Phone 1 - Value': 'Phone Number'
})

# Save the result
output_filename = "my_contacts.csv"
new_data.to_csv(output_filename, index=False)

print(f"Successfully created {output_filename}!")