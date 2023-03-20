# importing modules
import csv
import os
import sys
# csv import


filename ='template.csv'

df =[]
# opening the file 
with open(filename, 'r') as data:
    for line in csv.DictReader(data):
        df.append(line)
        print(line)













