# Question 1: Assign Serial Numbers to Internet Hubs
# You need to write a Python function to validate a given JSON object (or dictionary) against a specific schema and assign serial numbers to the hubs from a given range.
# The serial numbers must be assigned in reversed order based on the last digit of the hub IDs.
# Here's how to implement it


import json

# Define the allowed serial number range
serial_numbers = [f"C25CTW0000000000147{i}" for i in range(0, 9)][::-1]

# Function to assign serial numbers
def assign_serial_numbers(data):
    hubs = data.get("Internet_hubs", [])
    for hub in hubs:
        hub_id = hub["id"]
        last_digit = int(hub_id[-1])
        if 0 <= last_digit < len(serial_numbers):
            hub["serial_number"] = serial_numbers[last_digit]
    return data

# Function to validate the schema and assign serial numbers
def validate_and_assign(data):
    required_keys = ["id", "serial_number"]
    for hub in data.get("Internet_hubs", []):
        if not all(key in hub for key in required_keys):
            raise ValueError(f"Invalid schema for hub: {hub}")
    return assign_serial_numbers(data)

# Example JSON data
data = {
    "comment": "Do NOT commit local changes to this file to source control",
    "Internet_hubs": [
        {"id": "men1", "serial_number": "C25CTW00000000001470"},
        {"id": "mn1", "serial_number": "<serial number here>"},
        {"id": "mn2", "serial_number": "<serial number here>"},
        {"id": "mn3", "serial_number": "<serial number here>"},
        # Additional hubs here...
    ]
}

# Validate and assign serial numbers
updated_data = validate_and_assign(data)
print(json.dumps(updated_data, indent=4))
