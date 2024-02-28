import json
import numpy as np
from datetime import datetime

def AvgAge():
    file = open("presidents.json")
    Presidents = json.load(file)

    ages = []

    for year in Presidents:
        absyear = datetime.strptime(year['DOB'], '%Y-%m-%d')
        actualage = (2023 - absyear.year)
        ages.append(actualage) 
        Avgage = np.average(ages)
    print(Avgage)

AvgAge()