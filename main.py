import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the website to scrape
baseurl = 'https://example.com/shop/page/'
product_urls = []

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.3'
}

# Fetch product URLs from multiple pages
for page in range(1, 10):  # Adjust range as needed
    r = requests.get(f'{baseurl}{page}', headers=headers)  # Make a GET request to each page
    soup = BeautifulSoup(r.content, 'html.parser')  # Parse the HTML content using BeautifulSoup
    product_divs = soup.find_all('div', class_='product-detail-wrapper')  # Find all product detail divs
    
    for product_div in product_divs:
        a_tag = product_div.find('a', href=True)  # Find the first 'a' tag with an href attribute
        if a_tag:
            product_urls.append(a_tag['href'])  # Append the href (URL) to the product_urls list

# List to hold product details
product_details = []

# Extract h1 and price from each product URL
for url in product_urls:
    try:
        r = requests.get(url, headers=headers)  # Make a GET request to the product page
        soup = BeautifulSoup(r.content, 'html.parser')  # Parse the HTML content
        
        h1_tag = soup.find('h1')  # Find the h1 tag
        h1_text = h1_tag.get_text(strip=True) if h1_tag else 'N/A'  # Get the text of the h1 tag or 'N/A' if not found
        
        price_tag = soup.find('p', class_='price')  # Find the p tag with class 'price'
        price_text = price_tag.get_text(strip=True) if price_tag else 'N/A'  # Get the text of the price tag or 'N/A' if not found
        
        # Append the extracted details to the product_details list
        product_details.append({
            'Title': h1_text,
            'Price': price_text,
            'URL': url,
        })
    except requests.exceptions.RequestException as e:
        print(f'Request failed for URL {url}: {e}')  # Print error message if request fails
    time.sleep(1)  # Delay to prevent overloading the server

# Create a DataFrame from the product details
df = pd.DataFrame(product_details)

# Save the DataFrame to a CSV file
df.to_csv('product_details.csv', index=False)

print("Product details saved.")
