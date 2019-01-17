#!/usr/bin/env python3

from dateutil import parser
import re
from pprint import pprint

dates = open('dates', 'r')
dates_remaining = open('output/dates_remaining', 'w+')
dates_result = open('output/dates_result', 'w+')
dates_alpha = open('output/dates_alpha', 'w+')

default_date = '01/01/01'

alpha = []

dates_list = []
result_dates = {}
ex = []
for row in dates:
    dates_list.append(row.rstrip())

pprint(dates_list)


def is_empty(inp):
    return True if inp in ('', '0', '-', None) else False

def has_alpha(inp):
    return True if re.match(".*[a-zA-Z]+.*$", str(inp)) else False

def solve_alpha(date):
    alpha.append(date)
    dates_list.remove(date)

def solve_num(date):
    try:
        return(parser.parse(date))
    except:
        ex.append(date)
        return None

def parse_date():
    for date in dates_list:
        if is_empty(date):
            new_date = default_date
        elif has_alpha(date):
            solve_alpha(date)
        else:
            new_date = solve_num(date)
        if new_date:
            result_dates[date] = new_date
            # print(f'setting {date} -> {new_date}')
            dates_result.write(f"{date} -> {new_date}"+'\n')
            if date in dates_list:
                dates_list.remove(date)
            else:
                pass

parse_date()

for row in dates_list:
    dates_remaining.write(row+'\n')

for row in alpha:
    dates_alpha.write(row+'\n')


"""Extracting date"""
# import csv
# ans = []
# f = open('../filter1/without_alpha.csv', 'r', newline='')
# reader = csv.reader(f, delimiter=',', quotechar='"')
# for line in reader:
#     # print(type(line))
#     print(line)
#     ans.append(line[1])


# f1 = open('without_alpha', 'w+')
# for d in set(ans):
#     f1.write(d+"\n")



