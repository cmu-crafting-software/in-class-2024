import json
import csv

from datetime import datetime

def printYears():
    f = open("presidents.json")
    presidents = json.load(f)

    ages = []
    for president in presidents :
        birthyear = datetime.strptime(president['DOB'], '%Y-%m-%d')
        print(2024 - birthyear.year)

printYears()