import requests
import pandas
import subprocess
import sys

# additional code due to bs4 behaving unexpectedly when working with subprocess that interfered with docker
def install_bs4():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "bs4"])

try:
    from bs4 import BeautifulSoup
except:
    install_bs4()
    from bs4 import BeautifulSoup


def main():

    url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
    
    # web scrape contents from url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    header = []
    rows = []
    for i, row in enumerate(table.find_all('tr')):
        if i == 0:
            header = [el.text.strip() for el in row.find_all('th')]
        else:
            rows.append([el.text.strip() for el in row.find_all('td')])
        
    # find file corresponding to Last Modified '2022-02-07 14:03'
    last_modified_index = header.index("Last modified")
    name_index = header.index("Name")
    for row in rows:
        if len(row) == 4 and row[last_modified_index] == '2022-02-07 14:03':
            filename = row[name_index]
            break
        else:
            pass  

    # build URL required to download this file
    download_url = url + filename

    # download/write the file locally
    response = requests.get(download_url)
    open(filename, 'wb').write(response.content)

    # open file with pandas
    df = pandas.read_csv(filename)

    # find the records with the highest HourlyDryBulbTemperature and print result
    print(df.loc[[df.HourlyDryBulbTemperature.max()]])

    pass


if __name__ == "__main__":
    main()
