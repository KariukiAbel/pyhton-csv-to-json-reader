# import packages to read csv file and write a new json file

import csv, json

csvFilePath = 'path.csv'
jsonFilePath = 'path.json'

# read csv file and add data 
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['id']
        data[id] = rows
        
        
# create new json file and write data on it 
with open(jsonFilePath, 'w') as jsonFile:
    # make it more readable  and pretty
    jsonFile.write(json.dumps(data, indent=4))