import json
import urllib.request
from typing import Dict, Any


def fetch_json(url: str) -> Any:
    """Fetch JSON data from a URL.
    Returns parsed JSON or raises an exception on failure.
    """
    with urllib.request.urlopen(url) as response:
        if response.status != 200:
            raise RuntimeError(f"Failed to fetch {url}: HTTP {response.status}")
        charset = response.headers.get_content_charset() or "utf-8"
        data = response.read().decode(charset)
        return json.loads(data)


def fetch_market_data() -> Dict[str, Any]:
    """Collect minimal market data for digital collectibles and wearables.
    This function demonstrates fetching from two public placeholder APIs.
    Returns a dictionary with two keys: 'collectibles' and 'wearables'.
    """
    # Placeholder APIs – replace with real endpoints as needed.
    collectibles_url = "https://api.publicapis.org/entries?category=Games&https=true"
    wearables_url = "https://api.publicapis.org/entries?category=Health&https=true"

    collectibles = fetch_json(collectibles_url)
    wearables = fetch_json(wearables_url)

    return {
        "collectibles": collectibles,
        "wearables": wearables,
    }


if __name__ == "__main__":
    data = fetch_market_data()
    print(json.dumps(data, indent=2))
