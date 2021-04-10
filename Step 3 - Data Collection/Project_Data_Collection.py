# Web Scraping using Python to scrape data from website:

# Import packages (include in description):
import requests
from bs4 import BeautifulSoup
import time
import datetime
import sys
import logging
import zipfile

# Extract data from HTML webpage
URL = 'http://data.gdeltproject.org/gkg/index.html'
page = requests.get(URL)

# Create BeautifulSoup object to parse through HTML document
soup = BeautifulSoup(page.content, 'html.parser')

# Base url for file downloading
base_url = 'http://data.gdeltproject.org/gkg/'

# Iterate to obtain all 14 files we want to download based on "a" and "href" tags and write to file

for link in soup.find_all('a')[2:16]: # Do we still need to use array slicing?
    try:
        if link.has_attr('href'):
            file = link.attrs['href']
            # Create a list of dates to control which files to download:
            today = datetime.date.today()
            # List of dates:
            date_list = [today]
            # Add other dates
            for i in range(1, 8):
                new_day = today - datetime.timedelta(days=i)
                date_list.append()
            # Convert dates to string
            for date in date_list:
                date.strftime("%Y%d%m")
            logging.info('Will proceed to downloading the past week of files.')
            # 2) Loop through values that have the date within file name.
            for date in file:
                download_url = f"{base_url}{file}"
                with open(f"{file}", "wb") as file:
                    response = requests.get(download_url)
                    file.write(response.content)
                    logging.info('Files have been downloaded as ZIP.')
                    # Can try to read new file and convert to ZIP file (automate file unzipping):
                    with zipfile.ZipFile('/Users/jameshizon/Downloads/Open_Ended_Capstone_Project', 'r') as zip_ref:
                        zip_ref.extractall('/Users/jameshizon/Downloads/Open_Ended_Capstone_Project')
                        logging.info('Files have been unzipped.')
    except Exception as e:
        # Logging message
        logging.error(f"Error was {e}")





