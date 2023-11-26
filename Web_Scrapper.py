import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    # URL of the website to scrape
    url = 'http://quotes.toscrape.com'
    
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract data from the page
        quotes = []
        for quote in soup.find_all('span', class_='text'):
            quotes.append(quote.get_text())
        
        return quotes
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Call the function to scrape quotes
result = scrape_quotes()

# Print the scraped quotes
if result:
    for i, quote in enumerate(result, start=1):
        print(f"{i}. {quote}")
