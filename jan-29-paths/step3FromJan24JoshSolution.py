#!/usr/bin/env python3

import json
from datetime import datetime



def step3():
    f = open("presidents.json")
    presidents = json.load(f)

    ages = []
    for president in presidents :
        dob = datetime.strptime(president['DOB'], '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year
        if (today.month, today.day) <  (dob.month, dob.day) :
            age = age - 1
        ages.append(age)
    return ages

print(step3())