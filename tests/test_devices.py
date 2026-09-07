import os
import unittest

class TestDeviceDocs(unittest.TestCase):
    def test_docs_exist(self):
        self.assertTrue(os.path.exists('docs/devices.md'))

    def test_docs_content(self):
        with open('docs/devices.md', 'r') as f:
            content = f.read()
            self.assertIn('Device Compatibility', content)
            self.assertIn('Web3 Wallet Requirements', content)

if __name__ == '__main__':
    unittest.main()