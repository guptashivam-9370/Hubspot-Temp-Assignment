from hubspot import HubSpot
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
access_token = os.getenv('ACCESS_TOKEN')
api_client = HubSpot(access_token=access_token)

all_contacts = api_client.crm.contacts.get_all()
all_contacts = [contact.properties for contact in all_contacts]
for contact in all_contacts:
    print(contact)