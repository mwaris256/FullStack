import requests

try:
    # Attempt to use a basic function of the requests library
    response = requests.get("https://www.google.com")
    print("Requests library installed and functioning correctly!")
    print(f"Status Code: {response.status_code}")
except ImportError:
    print("Error: The 'requests' library could not be imported. It might not be installed.")
except Exception as e:
    print(f"An error occurred while using the requests library: {e}")