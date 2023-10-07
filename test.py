import requests
import json

# Your data as a Python dictionary
data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "password": "secretpassword"
}

# Convert the data to JSON format
json_data = json.dumps(data)

# Set the headers with 'Content-Type: application/json'
headers = {'Content-Type': 'application/json'}

# Make the POST request with the JSON data and headers
response = requests.post('http://127.0.0.1:5000/register', data=json_data, headers=headers)

# Check the response
if response.status_code == 201:
    print('User registered and logged in successfully.')
else:
    print(f'Error: {response.status_code} - {response.text}')
