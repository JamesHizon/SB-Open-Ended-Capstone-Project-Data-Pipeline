# Data Pipeline Class

# Standard Imports
import os
import datetime
import logging
import zipfile

# Third party imports
from bs4 import BeautifulSoup
import requests
import boto3


class DataPipeline:
    """
    This DataPipeline class will simply be used to take an website url as a data source and
    an S3 object as a possible data storage destination.

    The method that will be used is "extract_load_data()," which will take in
    """

    def __init__(self, s3_obj, url):
        """
        "__init__" method will simply take the listed inputs as well as create logging file
        to store logging metrics.

        :param s3_obj: S3 bucket object will be used to upload data in later method.
        :param url: Object will be used to scrape data.
        """
        self.s3_obj = s3_obj
        self.url = url
        # Create logging file
        logging.basicConfig(filename="dp_file.log", level=logging.DEBUG)
        logging.info("Data Pipeline has been created!")

    def extract_load_data(self, use_cloud, cloud_path):
        """
        This function will take an optional parameter "use_cloud" (BOOLEAN) and "cloud_path" to store files onto AWS S3.
        If the "use_cloud" parameter is true, then we will write to cloud location "cloud_path".
        For the case of Step 5 where we do not use cloud, we will simply set "use_cloud" to
        False and "cloud_path" can just be any variable since we are not using it.

        :return: Logging statement after extracting files from website.
        """
        # Extract data from HTML webpage
        url = self.url
        page = requests.get(url)
        # Create BeautifulSoup object to parse through HTML document
        soup = BeautifulSoup(page.content, "html.parser")
        # Base url for file downloading
        base_url = url[:-9]

        # Current Directory -> MAY NOT USE. -> CHANGE TO S3 BUCKET AS LOCATION.
        current_directory = os.getcwd()

        # Iterate to obtain all we want to download based on "a" and "href" tags and write to CSV file
        for link in soup.find_all("a"):
            try:
                if link.has_attr("href"):
                    # Obtain file name as string object:
                    file = link.attrs["href"]
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
                            # Download as zip file
                            with open(f"{file}", "wb") as zip_file:
                                response = requests.get(download_url)
                                # Write content to zip_file
                                zip_file.write(response.content)
                                logging.info(f"Filename of '{file}' has been downloaded.")
                                # Deal with both cases (using AWS or not)
                                if use_cloud is False:
                                    # Use after creating zipfile to unpack as a CSV
                                    with zipfile.ZipFile(f"{file}", "r") as zip_ref:
                                        # INSTEAD OF EXTRACTING ALL TO CURRENT DIRECTORY, WE MAY NEED TO
                                        # UPLOAD DIRECTLY TO S3 (THIS IS THE STEP WHERE WE WILL UPLOAD TO S3.
                                        zip_ref.extractall(current_directory)
                                else:
                                    # Load file to cloud path if use_cloud parameter is True
                                    # (I will update this part of the code later on to deal w/ S3 bucket).
                                    with zipfile.ZipFile(f"{file}", "r") as zip_ref:
                                        zip_ref.extractall(cloud_path)
                            logging.info("File has been downloaded and unpacked as CSV.")
                logging.info("All files have been downloaded.")
            except Exception as e:
                logging.error(f"Error was {e}")


# Create s3 object using boto3
s3 = boto3.client('s3')

# Obtain url
website_url = "http://data.gdeltproject.org/gkg/index.html"

# Create data pipeline (use s3 object as input)
dp = DataPipeline(s3, website_url)

# Run extract_load_data method to scrape and download the data from HTML document
dp.extract_load_data(use_cloud=False, cloud_path=None)
