# Import the requests library to make HTTP requests
import requests

# Prompt the user to input the name of the city they want to check the weather for
city = input("Enter the name of the city: ")

# Construct the URL for the Weather API using an f-string to insert the city and the API key
url = f"https://api.weatherapi.com/v1/current.json?key=82ce39ae0e5e42efa4e35904240109&q={city}"

# Send an HTTP GET request to the API endpoint
r = requests.get(url)

# Print the response text, which contains the weather data in JSON format
print(r.text)
