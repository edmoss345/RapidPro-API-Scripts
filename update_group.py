import pandas as pd
import json
from temba_client.v2 import TembaClient

# Load credentials from JSON file
with open('api_credentials.json', 'r') as f:
    credentials = json.load(f)

api_url = credentials['api_url']
api_token = credentials['api_token']

# Initialize the TembaClient with the loaded credentials
client = TembaClient(api_url, api_token)

# Read the Excel file into a pandas DataFrame
excel_file_path = 'C:/Users/edmun/OneDrive - EEM Engineering Ltd/IDEMS/RCT/Creating Test Group/Test Group.xlsx'
df = pd.read_excel(excel_file_path, sheet_name='test group')

new_group = "7month first batch"

# Loop through each row in the DataFrame
for _, row in df.iterrows():
    contact_uuid = row['UUID']
    
    # Fetch the contact's current data
    contact_data = client.get_contacts(uuid=contact_uuid).first()
    
    if not contact_data:
        print(f"No data found for contact {contact_uuid}")
        continue
    
    # Get current group names
    group_names = [group.name for group in contact_data.groups]

    # Remove any problem group
    problem_group = "completed 3 month"
    if problem_group in group_names:
        group_names.remove(problem_group)
    
    # Add the new group if not already present
    if new_group not in group_names:
        group_names.append(new_group)
        client.update_contact(contact_uuid, groups=group_names)
        print(f"Added group '{new_group}' to contact {contact_uuid}")
    else:
        print(f"Contact {contact_uuid} already in group '{new_group}', no update needed.")
