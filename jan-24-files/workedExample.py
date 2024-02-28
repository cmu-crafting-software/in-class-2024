import json
import csv

from datetime import datetime

def printYears():
    f = open("constitutional_amendments.json")
    amendments = json.load(f)

    ages = []
    for amendment in amendments :
        ratified = datetime.strptime(amendment['Ratified'], '%m/%d/%Y')
        print(ratified.year)

def printCSV():
    with open('presidents.csv', newline='') as csvfile:
        amendments = csv.reader(csvfile, delimiter=',', quotechar='|')
        totalage = 0
        count = 0
        #skip header row
        next(amendments);

        for amendment in amendments :
            totalage = totalage + datetime.strptime(amendment[2], '%Y-%m-%d').year
            count = count + 1
        print(totalage/count)

def printCSVDict():
    with open('constitutional_amendments.csv', newline='') as csvfile:
        amendments = csv.DictReader(csvfile)

        for amendment in amendments :
            print(datetime.strptime(amendment['Proposed'], '%m/%d/%Y').year)

#printYears()

printCSV()

#printCSVDict()
