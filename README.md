# Project Setup Guide for Populating a CRM database
#### with Dummy data
Follow these steps to set up and run the project:

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Create a `.env` File

Create a `.env` file in the project root directory with the following content:

```
ACCESS_TOKEN = <access_token>
```

Replace `<access_token>` with your actual access token.
## 2.1. Data Format

```json
[
    {
        "name": "string",
        "email": "string",
        "phone": "string",
        "address": "string",
        "Note 1": "string",
        "Note 2": "string"
        },
        ...
    ]
    ```

    Each object represents a CRM contact with fields such as `name`, `email`, `phone`, `address`, `note_1`, and `note_2`.

    Ensure that these columns are added in CRM database before running the script.

    The generated dummy data will be saved in a CSV file named `dummy_contacts.csv` in the project root directory, with columns corresponding to the same fields.
## 3. Generate Dummy Data

Run the following command to generate data:

```bash
python generate_data.py
```

## 4. Send Data

Send the generated data using:

```bash
python send_data.py
```

## 5. Get Data

Retrieve data by running:

```bash
python get_data.py
```

---