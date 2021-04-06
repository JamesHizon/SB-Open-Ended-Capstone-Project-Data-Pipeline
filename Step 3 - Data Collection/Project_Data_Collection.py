# Web Scraping using Python to scrape data from website:

# Steps:
# 1) Use requests package to run an HTTP request to retrieve HTML data.
# - This will allow the server to send back and store the data inside a Python object.
# 2) Build BeautifulSoup object to parse through objects of web page within HTML format.
# 3) Work with base_url to link through each file that we want to download and implement Python slicing
# to obtain only 14 files.

import requests
from bs4 import BeautifulSoup
from time import time

# Extract data from HTML webpage
URL = 'http://data.gdeltproject.org/gkg/index.html'
page = requests.get(URL)

# Create BeautifulSoup object to parse through HTML document
soup = BeautifulSoup(page.content, 'html.parser')

# Base url for file downloading
base_url = 'http://data.gdeltproject.org/gkg/'

# Iterate to obtain all 14 files we want to download based on "a" and "href" tags
for link in soup.find_all('a')[2:16]:
    # Count time it takes to download each link
    print("Start Execution : ")
    time.ctime()  # Initialize time object to return time string
    file_link = link.get('href')
    if link.has_attr('href'):
        file = link.attrs['href']
        # Create "download_url" object from list of file names (file) and base_url
        download_url = f"{base_url}{file}"
        # Introduce time object inside context manager to track file download time
        with open(f"{file}", 'wb') as file:
            response = requests.get(download_url)
            file.write(response.content)
            # Stop execution time
            print("Stop Execution : ", end="")
            print(time.ctime())





