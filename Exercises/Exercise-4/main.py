import glob
import json
import pandas as pd
from flatten_json import flatten


def main():
    #crawl the datadirectory and identify all json files
    file_paths = []
    for file in glob.glob("data/**/*.json", recursive=True):
        file_paths.append(file)

    for file in file_paths:

        # Read json data (to a dictionary)
        with open(file) as f:
            data = json.load(f)

        # Flatten data
        flat_data = flatten(data, '_')
        
        # Convert flat json data to pandas DataFrame
        df = pd.DataFrame([flat_data])

        # Get file name from original file
        filename = file.split('\\')[-1][:-5]
        
        # Write DataFrame to a csv file
        df.to_csv(filename+'.csv', index=False)
    pass


if __name__ == "__main__":
    main()
