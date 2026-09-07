import requests
import json

# Fetch data from public APIs

def fetch_digital_collectibles_data():
    url = 'https://api.example.com/digital-collectibles'
    response = requests.get(url)
    return response.json()

def fetch_wearable_tech_data():
    url = 'https://api.example.com/wearable-tech'
    response = requests.get(url)
    return response.json()

# Save data to JSON files

def save_data(data, filename):
    with open(f'research/data/{filename}.json', 'w') as file:
        json.dump(data, file)

# Main research function

def conduct_research():
    collectibles_data = fetch_digital_collectibles_data()
    wearable_data = fetch_wearable_tech_data()
    save_data(collectibles_data, 'digital_collectibles')
    save_data(wearable_data, 'wearable_tech')

if __name__ == '__main__':
    conduct_research()
