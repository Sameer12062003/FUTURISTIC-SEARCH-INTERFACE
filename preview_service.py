import requests
from bs4 import BeautifulSoup

def fetch_webpage_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        return str(soup)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
