# Web Scraping using Python to scrape data from website:

# Import packages
import requests
from bs4 import BeautifulSoup
import datetime
import logging
import zipfile
import os

# Control logging levels:
logging.basicConfig(level=logging.INFO)

# Extract data from HTML webpage
URL = 'http://data.gdeltproject.org/gkg/index.html'
page = requests.get(URL)

# Create BeautifulSoup object to parse through HTML document
soup = BeautifulSoup(page.content, 'html.parser')

# Base url for file downloading
base_url = 'http://data.gdeltproject.org/gkg/'

# Current Directory
current_directory = os.getcwd()

# Iterate to obtain all 14 files we want to download based on "a" and "href" tags and write to file

for link in soup.find_all('a')[2:16]: # Do we still need to use array slicing?
    try:
        if link.has_attr('href'):
            # Obtain file name as string object:
            file = link.attrs['href']
            # Create a list of dates to control which files to download:
            today = datetime.date.today()
            # List of dates:
            date_list = [today]
            # Add other dates (within 1 week):
            for i in range(1, 8):
                new_day = today - datetime.timedelta(days=i)
                date_list.append(new_day)
            # Convert dates to string to filter file name
            for date in date_list:
                date = date.strftime("%Y%m%d")
                if date in file:
                    download_url = f"{base_url}{file}"
                    with open(f"{file}", "wb") as zip_file:
                        response = requests.get(download_url)
                        zip_file.write(response.content)
                    logging.info("Zip file has been downloaded.")
                    # Use after creating zipfile to unpack as a CSV
                    with zipfile.ZipFile(f"{file}", "r") as zip_ref:
                        zip_ref.extractall(current_directory)
                    logging.info("File has been downloaded and unpacked as CSV.")
        logging.info("All files have been downloaded.")
    except Exception as e:
        logging.error(f"Error was {e}")













