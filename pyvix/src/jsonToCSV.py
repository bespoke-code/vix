import json
import csv
import argparse
import sys


def init():
    parser = argparse.ArgumentParser(
        description="A JSON to CSV file parser."
    )
    parser.add_argument(
        'inputFile',
        metavar='inputFile',
        help='A JSON-formatted input file.'
    )
    parser.add_argument(
        'outputFile',
        metavar='outputFile',
        help='A pathname for storing the output file.'
    )
    return parser


def jsonToCSV(jsonFile, outputCSV):
    try:
        datasetJSON = open(jsonFile, 'r')
    except:
        print("Can't open the dataset! Exiting NOW")
        sys.exit(1)
    inputFile = json.load(datasetJSON)

    csvFile = open(outputCSV, 'w', newline='')
    csvWriter = csv.DictWriter(
        csvFile,
        fieldnames=['Dataset Name', 'Keywords', 'Theme', 'Profession', 'Recommendation']
    )
    datasets=inputFile["dataset"]
    professions = [
        'Teacher',
        'Physicist',
        'Farmer',
        'Biologist',
        'Power Engineer'
    ]
    for i in range(len(datasets)):
        if i == 0:
            csvWriter.writeheader()
        for profession in professions:
            csvWriter.writerow(
                {
                    'Dataset Name': datasets[i]["title"],
                    'Keywords': datasets[i]["keyword"],
                    'Theme': datasets[i]["theme"],
                    'Profession': profession,
                    'Recommendation': '0'
                }
            )
    datasetJSON.close()
##############################################################################
if __name__ == '__main__':
    #args = init().parse_args()
    #jsonToCSV(args.inputFile, args.outputFile)
    jsonToCSV("/home/andrej/git/vix/pyvix/datasets/data-nasa-subset.json", "/home/andrej/git/vix/pyvix/datasets/data-nasa-subset.csv")
    #print(data["dataset"][0].keys())
