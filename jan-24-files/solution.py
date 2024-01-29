import json
import csv

from datetime import datetime

def averageAge():
    f = open("jan-24-files/presidents.json")
    presidents = json.load(f)

    ages = []
    for president in presidents :
        # age = 2024 - int(president["DOB"][:4])
        age = 2024 - datetime.strptime(president["DOB"],'%Y-%m-%d').year
        ages.append(age)
    print(sum(ages)/len(ages))

#         # ratified = datetime.strptime(amendment['Ratified'], '%m/%d/%Y')
#         # print(ratified.year)

# def printCSV():
#     with open('constitutional_amendments.csv', newline='') as csvfile:
#         amendments = csv.reader(csvfile, delimiter=',', quotechar='|')

#         #skip header row
#         next(amendments);

#         for amendment in amendments :
#             print(datetime.strptime(amendment[2], '%m/%d/%Y').year)

# def printCSVDict():
#     with open('constitutional_amendments.csv', newline='') as csvfile:
#         amendments = csv.DictReader(csvfile)

#         for amendment in amendments :
#             print(datetime.strptime(amendment['Proposed'], '%m/%d/%Y').year)

# printYears()

# printCSV()

# printCSVDict()
averageAge()


1. find all files with .json extension in my folder (including subdirectory)
2. store those file paths (files =[])
3. loop through those files, read .json file, and extract age from those files



ages = [] 
for file in files:
    # json read
    f= json.load(file)
    for obj in f:
        age = obj['age']
        ages.append(age)
print(sum(ages)/len(ages))