import requests
from bs4 import BeautifulSoup

class DigitalCollectiblesResearch:
    def __init__(self):
        self.base_url = 'https://example.com/api/digital-collectibles'

    def fetch_market_trends(self):
        response = requests.get(f'{self.base_url}/market-trends')
        return response.json()

    def fetch_consumer_behavior(self):
        response = requests.get(f'{self.base_url}/consumer-behavior')
        return response.json()

    def fetch_emerging_technologies(self):
        response = requests.get(f'{self.base_url}/emerging-technologies')
        return response.json()

    def fetch_potential_use_cases(self):
        response = requests.get(f'{self.base_url}/potential-use-cases')
        return response.json()

    def scrape_website(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
