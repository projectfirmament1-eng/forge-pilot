import pytest

def test_device_categories():
    expected_categories = [\'Apple Watch\', \'Wear OS\', \'Garmin\', \'Samsung Galaxy Watch\']
    with open(\'research/device_compatibility.md\') as f:
        content = f.read()
    for category in expected_categories:
        assert category in content
