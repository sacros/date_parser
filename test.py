#!/usr/bin/env python3
import csv
import re


original_f = open('test.csv', 'r', newline='')
original_reader = csv.reader(original_f, delimiter=',', quotechar='"')

counter = 1

for row in original_reader:
    print(f"row#{counter}: {row}")
    counter += 1
    print(row[4].replace("\n", "$"))
