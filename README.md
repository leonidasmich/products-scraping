# Web Scraper for Product Details

This project is a web scraping script that extracts product details such as title and price from a website and saves the information into a CSV file. The script uses Python libraries such as `requests`, `BeautifulSoup`, and `pandas` to perform the scraping and data storage tasks.

## Overview

The script performs the following tasks:
1. Fetches the HTML content of multiple pages from a given base URL.
2. Extracts product URLs from each page.
3. Visits each product URL to extract the product title (`h1` tag) and price (`p` tag with class `price`).
4. Stores the extracted data in a pandas DataFrame.
5. Saves the DataFrame to a CSV file named `product_details.csv`.

## Why This is Useful

Web scraping is useful for a variety of reasons:
- **Data Collection**: Automatically gather large amounts of data from websites without manual effort.
- **Market Analysis**: Track product prices and availability across different websites for competitive analysis.
- **Research**: Collect data for research purposes, such as sentiment analysis or trend tracking.

## Dependencies

The script requires the following Python libraries:
- `requests`: To make HTTP requests to the website.
- `BeautifulSoup`: To parse HTML content and extract information.
- `pandas`: To manipulate and save the extracted data.

You can install these dependencies using `pip`:
```bash
pip install -r requirements.txt
