import requests

# Define the URL for the API endpoint
url = "http://127.0.0.1:8000/v1/insert"

# Define the data to be sent in the request body
data = {
    "userId": "4",
    "phone": "+84709999888",
    "name": "demo4"
}

# Send the POST request with the data
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("User created successfully!")
    user_data = response.json().get("data")
    print("Created user:", user_data)
else:
    print("Failed to create user. Status code:", response.status_code)
    print("Error message:", response.json().get("message"))
