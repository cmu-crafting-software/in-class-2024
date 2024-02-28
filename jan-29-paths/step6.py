import json
import os

import glob

from datetime import datetime

def cal_age(dob):
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.now()
    return (today - birth_date).days //365

def avg_age(files):
    total_age = 0
    count = 0

    for file in files:
        with open(file,'r') as json_file:
            data = json.load(json_file)
            for person in data:
                if 'DOB' in person:
                    age = cal_age(person['DOB'])
                    total_age += age
                    count += 1
    return total_age / count if count >0 else None

files = glob.glob('**/*.json', recursive=True)
print(files)

average_age = avg_age(files)
print(average_age)
