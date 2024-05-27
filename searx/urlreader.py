from bs4 import BeautifulSoup
import requests

class UrlReader():

    def fetch_html(self, url, headers):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Ensure we notice bad responses
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    from bs4 import BeautifulSoup

    def extract_text(self, html):
        if html is None:
            return "No HTML to parse"

        soup = BeautifulSoup(html, 'html.parser')
        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        # Get text
        text = soup.get_text(separator=' ', strip=True)
        return text

    def get_content(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36', 'Cookie' : ''}
        html_content = self.fetch_html(url, headers)
        # sc = YoutubeScraper()
        # html_content = sc.run(url)
        plain_text = self.extract_text(html_content)
        return plain_text

    