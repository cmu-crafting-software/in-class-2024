#!/usr/bin/env python3

import json
import os
import glob
from datetime import datetime



def step3():
    f = open("presidents.json")
    presidents = json.load(f)
    new_list = sorted(presidents, key=lambda x: x.birthstate)
    ages = []
    for president in presidents :
        dob = datetime.strptime(president['DOB'], '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year
        if (today.month, today.day) <  (dob.month, dob.day) :
            age = age - 1
        ages.append(age)
    return ages


def rockmusicians():
    os.chdir("musicians/rock")
    files = glob.glob('*')
    for file in files :
        print(file)
    print(files)

#print(step3())

rockmusicians()