import pytest
from research.digital_collectibles_research import DigitalCollectiblesResearch

@pytest.fixture
def research_instance():
    return DigitalCollectiblesResearch()

class TestDigitalCollectiblesResearch:
    def test_fetch_market_trends(self, research_instance):
        trends = research_instance.fetch_market_trends()
        assert isinstance(trends, dict)

    def test_fetch_consumer_behavior(self, research_instance):
        behavior = research_instance.fetch_consumer_behavior()
        assert isinstance(behavior, dict)

    def test_fetch_emerging_technologies(self, research_instance):
        technologies = research_instance.fetch_emerging_technologies()
        assert isinstance(technologies, dict)

    def test_fetch_potential_use_cases(self, research_instance):
        use_cases = research_instance.fetch_potential_use_cases()
        assert isinstance(use_cases, dict)

    def test_scrape_website(self, research_instance):
        text = research_instance.scrape_website('https://example.com')
        assert isinstance(text, str)
