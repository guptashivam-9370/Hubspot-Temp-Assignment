from faker import Faker
import csv
import random

def generate_data():
    fake = Faker()
    data = []
    for _ in range(100):
        contact = {
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'address': fake.address(),
            'Note 1': fake.sentence(),
            'Note 2': fake.sentence(),
        }
        data.append(contact)
    return data

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    generated_data = generate_data()
    save_to_csv(generated_data, 'dummy_contacts.csv')