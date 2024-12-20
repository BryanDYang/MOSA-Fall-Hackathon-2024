import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OSI_API_KEY = os.getenv("OSI_API_KEY")

BASE_URL = "https://api.opensustainabilityindex.org/v1"

def get_industries():
    """Fetch a list of industries from the OSI API."""
    url = f"{BASE_URL}/industries"
    params = {
        "api-key": OSI_API_KEY,
        "limit": 300,
        "offset": 0,
        "order": "desc"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("data", [])

def get_companies_by_industry(industry_name):
    """Fetch companies associated with a specific industry."""
    url = f"{BASE_URL}/companies"
    params = {
        "api-key": OSI_API_KEY,
        "industry": industry_name,
        "limit": 300,
        "offset": 0,
        "order": "desc"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("data", [])

# Example usage
if __name__ == "__main__":
    industries = get_industries()
    print("Industries:", industries[:5])  # Print the first 5 industries
