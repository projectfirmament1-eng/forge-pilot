import pytest
from unittest.mock import patch
import research_script

# Mocking API responses

@patch('requests.get')
def test_fetch_digital_collectibles_data(mock_get):
    mock_get.return_value.json.return_value = {'items': [{'id': 1, 'name': 'Collectible 1'}]}
    result = research_script.fetch_digital_collectibles_data()
    assert result == {'items': [{'id': 1, 'name': 'Collectible 1'}]}

@patch('requests.get')
def test_fetch_wearable_tech_data(mock_get):
    mock_get.return_value.json.return_value = {'devices': [{'id': 1, 'type': 'Smartwatch'}]}
    result = research_script.fetch_wearable_tech_data()
    assert result == {'devices': [{'id': 1, 'type': 'Smartwatch'}]}
