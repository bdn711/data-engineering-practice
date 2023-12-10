import requests
import os
from pathlib import Path
from zipfile import ZipFile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    # create the directory downloads if it doesn't exist
    downloads_dir = Path('downloads')
    downloads_dir.mkdir(exist_ok=True)
    
    # change current working directory to the newly created downloads folder
    os.chdir(str(downloads_dir))
    
    for uri in download_uris:

        try:
            # download files one by one
            response = requests.get(uri)

            # split out filename from the uri
            zip_filename = uri.split('/')[-1]

            # save downloaded file using filename
            open(zip_filename, 'wb').write(response.content)

        except:
            pass

    pass


if __name__ == "__main__":
    main()
