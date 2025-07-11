import pandas as pd
import json
from temba_client.v2 import TembaClient

# Load credentials from JSON file
with open("api_credentials.json", "r") as f:
    credentials = json.load(f)

api_url = credentials["api_url"]
api_token = credentials["api_token"]

# Initialize the TembaClient with the loaded credentials
client = TembaClient(api_url, api_token)

# Read the Excel file into a pandas DataFrame
excel_file_path = "./Excel files/june_13_no_waiting_list.xlsx"
df = pd.read_excel(excel_file_path, sheet_name="Sheet1")

new_group = "missed waiting list"

# Step 1: Build a lookup of all groups
group_lookup = {group.name: group for group in client.get_groups().all()}

# Step 2: Create the new group if it doesn't exist
if new_group not in group_lookup:
    client.create_group(new_group)
    print(f"✅ Created new group: '{new_group}'")
    # Refresh the group lookup
    group_lookup = {group.name: group for group in client.get_groups().all()}

# Step 3: Process each contact
for _, row in df.iterrows():
    contact_uuid = row["UUID"]

    # Fetch contact data
    contact_data = client.get_contacts(uuid=contact_uuid).first()

    if not contact_data:
        print(f"❌ No data found for contact {contact_uuid}")
        continue

    # Filter to only static groups (non-query)
    # Query groups are managed from logic in workspce so we do not want to include here
    group_names = []
    for group_ref in contact_data.groups:
        group_obj = group_lookup.get(group_ref.name)
        if group_obj and not group_obj.query:
            group_names.append(group_ref.name)

    # Add new group if not already present
    if new_group not in group_names:
        group_names.append(new_group)
        client.update_contact(contact_uuid, groups=group_names)
        print(f"✅ Added group '{new_group}' to contact {contact_uuid}")
    else:
        print(
            f"ℹ️ Contact {contact_uuid} already in group '{new_group}', no update needed."
        )
