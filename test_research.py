import unittest
from research import fetch_market_data

class TestResearch(unittest.TestCase):
    def test_fetch_market_data_structure(self):
        data = fetch_market_data()
        # Expect top-level keys
        self.assertIn('collectibles', data)
        self.assertIn('wearables', data)
        # Basic sanity: each should be a dict with 'count' key from publicapis.org response
        for key in ('collectibles', 'wearables'):
            self.assertIsInstance(data[key], dict)
            self.assertIn('count', data[key])
            self.assertIsInstance(data[key]['count'], int)

if __name__ == '__main__':
    unittest.main()
