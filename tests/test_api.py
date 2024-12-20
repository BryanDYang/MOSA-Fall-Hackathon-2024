import os
import requests
from dotenv import load_dotenv  # only necessary if using .env files

# Load environment variables from .env if you're using it
load_dotenv()

OSI_API_KEY = os.getenv("OSI_API_KEY")

base_url = "https://api.opensustainabilityindex.org/v1"

def test_get_industries():
    url = f"{base_url}/industries"
    params = {
        "api-key": OSI_API_KEY,
        "limit": 10,
        "offset": 0,
        "order": "desc"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data

if __name__ == "__main__":
    industries_data = test_get_industries()
    print("Sample response from OSI Industries endpoint:", industries_data)
