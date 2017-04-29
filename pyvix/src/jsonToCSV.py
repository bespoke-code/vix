import json
import csv
import argparse

def init():
    parser=argparse.ArgumentParser(description="A JSON to CSV file parser.")
    parser.add_argument('inputFile', metavar='inputFile', help='A JSON-formatted input file.')
    parser.add_argument('outputFile', metavar='outputFile', help='A pathname for storing the output file.')
    return parser

def jsonToCSV(jsonFile):
    inputFile = json.load(jsonFile)

    csvFile = csv.W

if __name__ == '__main__':
    args = init().parse_args()
    jsonToCSV(args.inputFile, args.outputFile)