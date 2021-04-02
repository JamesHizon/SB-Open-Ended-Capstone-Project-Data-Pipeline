# Web Scraping using Python to scrape data from website:

# Steps:
# 1) Use requests package to run an HTTP request to retrieve HTML data.
# - This will allow the server to send back and store the data inside a Python object.
# 2) Build BeautifulSoup object to parse through objects of web page within HTML format.
# 3) Work with base_url to link through each file that we want to download and implement Python slicing
# to obtain only 14 files.

import requests
from bs4 import BeautifulSoup

URL = 'http://data.gdeltproject.org/gkg/index.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

base_url = 'http://data.gdeltproject.org/gkg/'

for link in soup.find_all('a')[2:16]:
    file_link = link.get('href')
    if link.has_attr('href'):
        file = link.attrs['href']
        download_url = f"{base_url}{file}"
        with open(f"{file}", 'wb') as file:
            response = requests.get(download_url)
            file.write(response.content)





