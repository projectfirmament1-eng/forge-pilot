import unittest
from pathlib import Path

class TestResearchReport(unittest.TestCase):
    def test_report_exists(self):
        report_path = Path('/tmp/forge-work/5b3fd4cb-c718-4eb6-9863-5aa058fb525b/research_report.md')
        self.assertTrue(report_path.exists(), 'Research report file does not exist')

    def test_report_content(self):
        with open('/tmp/forge-work/5b3fd4cb-c718-4eb6-9863-5aa058fb525b/research_report.md', 'r') as file:
            content = file.read()
            self.assertIn('Digital Collectibles', content, 'Report missing Digital Collectibles section')
            self.assertIn('Wearable Technology', content, 'Report missing Wearable Technology section')

if __name__ == '__main__':
    unittest.main()