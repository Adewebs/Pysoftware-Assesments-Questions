#Question 2: API Service to Retrieve and Validate Customer Addresses
# You need to write a Python function that retrieves customer addresses using a given API, validates the data, and saves it in CSV format.
#

import csv
import requests

API_KEY = "ssfdsjfksjdhfgjfgvjdshgvshgkjsdlgvkjsdgjkl"
BASE_URL = "https://pysoftware.com/v1" #kindly replace with any baseurl of choice
HEADERS = {"X-API-KEY": API_KEY}

# Function to get total number of customers
def get_customer_count():
    response = requests.get(f"{BASE_URL}/customer_numbers", headers=HEADERS)
    return int(response.text)

# Function to get customer address by customer number
def get_customer_address(customer_number):
    response = requests.get(f"{BASE_URL}/address_inventory/{customer_number}", headers=HEADERS)
    return response.json()

# Validate and clean address
def validate_address(address):
    required_fields = ["id", "first_name", "last_name", "street", "postcode", "state", "country"]
    for field in required_fields:
        if field not in address or not address[field]:
            raise ValueError(f"Invalid address field: {field}")
    return address

# Save addresses to CSV file
def save_addresses_to_csv(addresses, filename):
    keys = addresses[0].keys()  # Assumes all addresses have the same structure
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(addresses)
    print(f"Addresses saved to {filename}")

# Main function to retrieve, validate, and save addresses
def retrieve_and_save_addresses():
    customer_count = get_customer_count()
    all_addresses = []

    for customer_number in range(1, customer_count + 1):
        try:
            address = get_customer_address(customer_number)
            validated_address = validate_address(address)
            all_addresses.append(validated_address)
        except Exception as e:
            print(f"Error processing customer {customer_number}: {e}")

    save_addresses_to_csv(all_addresses, "customer_addresses.csv")
    return all_addresses

# Execute the function
addresses = retrieve_and_save_addresses()
