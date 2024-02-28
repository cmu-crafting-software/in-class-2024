#!/usr/bin/env python3


import csv
from datetime import datetime
import os

def sortPresHeights(presHeights):
   print(presHeights)
   n = len(presHeights)
    # Traverse through all array elements
   for i in range(n):
        # Last i elements are already in place
       for j in range(0, n-i):
           # Swap if the element found is greater
           # than the next element
           if presHeights[j][1] > presHeights[j+1][1] :
               presHeights[j], presHeights[j+1] = presHeights[j+1], presHeights[j]

   return presHeights

def calc_avg_h():
   totalHeight = 0
   heights = []
   numRows = 0
   greatness = []
   with open ('./feb-12-debugging/president_heights.csv') as csvfile:
       presidentReader = csv.DictReader(csvfile, delimiter = ",")
       for row in presidentReader:
           presName = row['name']
           numRows = numRows +1  
           currheight = int(row['height(cm)'])
           heights.append((presName,currheight))
           totalHeight +=  currheight
        #    greatnessvalue = row['“Greatness Ranking"']
        #    if (greatnessvalue.isdigit()):
        #        greatnessvalue = int(greatnessvalue)
        #        greatness.append(greatnessvalue)
          
         
   #find quartiles of "greatness"
#    for i in range(len(greatness)):
#        for j in range(0, len(greatness)-i-1):
#            if greatness[j] > greatness[j+1] :
#                greatness[j], greatness[j+1] = greatness[j+1], greatness[j]      
#    print(greatness)
#    medianGreatness = greatness[int(len(greatness)/2)]
   print(heights)
#    print(medianGreatness)
#    sortPresHeights(heights)
#    assert numRows == 10
   return totalHeight/numRows


def main():
   print(os.getcwd())
   with open ('./feb-12-debugging/president_heights.csv') as csvfile:
       presidentReader = csv.DictReader(csvfile, delimiter = ",")
       for row in presidentReader:
           print(row['name'])
       print(calc_avg_h())








def test_calc_avg_h():
   print(calc_avg_h())
   #assert calc_avg_h == 5




if __name__ == "__main__":
   main()
