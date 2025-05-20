from hubspot import HubSpot
from dotenv import load_dotenv
import os
import pandas as pd
from hubspot.crm.contacts import BatchInputSimplePublicObjectBatchInput, SimplePublicObjectInput
load_dotenv()
access_token = os.getenv('ACCESS_TOKEN')
api_client = HubSpot(access_token=access_token)

def import_data():
    df = pd.read_csv('dummy_contacts.csv')
    batch_size = 10
    total_imported = 0
    for i in range(0, len(df), batch_size):
        batch = df[i:i + batch_size]
        contact_batch = []
        for index, row in batch.iterrows():
            properties = {
                "email": row["email"],
                "firstname": row["name"].split()[0].lower(),
                "lastname": row["name"].split()[1].lower(),
                "phone": row["phone"],
                "address": row["address"].lower(),
                "note_1": row["Note 1"],
                "note_2": row["Note 2"],
            }
            # print(properties)
            contact_batch.append(SimplePublicObjectInput(
                properties=properties
            ))

        try:
            batch_input = BatchInputSimplePublicObjectBatchInput(
                inputs=contact_batch
            )
            # print(batch_input)
            response = api_client.crm.contacts.batch_api.create(
                batch_input_simple_public_object_batch_input_for_create=batch_input
            )
            total_imported += len(batch)
            print(f"Successfully imported Total: {total_imported}/{len(df)}")
        except Exception as e:
            print(f"Error importing batch starting at index {i}: {e}")
            return total_imported
    return total_imported

if __name__ == "__main__":
    total_imported = import_data()
    print(f"Total contacts imported: {total_imported}")