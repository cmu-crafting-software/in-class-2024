import json
import csv

def s_sort(s):
    return s['BirthState']

f = open('presidents.json')
#print(f)
presidents = json.load(f)

presidents.sort(key=s_sort)

print(presidents)