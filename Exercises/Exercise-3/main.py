import boto3
import gzip


def main():

    # boto3 download the file from s3 located at bucket commoncrawl and key 
    # crawl-data/CC-MAIN-2022-05/wet.paths.gz
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.download_file(
        'commoncrawl',
        'crawl-data/CC-MAIN-2022-05/wet.paths.gz',
        'wet.paths.gz'
        )


    # Extract and open this file with Python and pull uri from the first line
    with gzip.open('wet.paths.gz', 'rt') as file:
        uri = file.readline().strip()

    # Download the uri file (from first file line) from s3 using boto3
    filename = uri.split('/')[-1]
    s3.download_file(
        'commoncrawl',
        uri,
        filename
        )

    # Print each line to terminal
    with gzip.open('wet.paths.gz', 'rt') as file:
        for line in file:
            print(line)

    pass


if __name__ == "__main__":
    main()
