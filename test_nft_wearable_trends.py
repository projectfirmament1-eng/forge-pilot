import unittest
from nft_wearable_trends import analyze_trends, generate_report

class TestNFTSync(unittest.TestCase):

    def test_analyze_trends(self):
        trends = analyze_trends()
        self.assertTrue(isinstance(trends, dict))
        self.assertIn('market_insights', trends)
        self.assertIn('tech_advancements', trends)
        self.assertIn('consumer_preferences', trends)

    def test_generate_report(self):
        report = generate_report()
        self.assertTrue(isinstance(report, str))
        self.assertIn('NFT Wearable Trends 2024 Report', report)
        self.assertIn('Key Insights:', report)
        self.assertIn('Sources:', report)

if __name__ == '__main__':
    unittest.main()
