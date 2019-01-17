#!/usr/bin/env python3
import csv
import re

def is_empty(inp):
    return True if inp in ('', 0, '0', None) else False

def has_alpha(inp):
  return True if re.match(".*[a-zA-Z]+.*$", str(inp)) else False

"""is_empty Test Cases"""
# print(is_empty(""))
# print(is_empty("asd"))
# print(is_empty(''))
# print(is_empty('09'))
# print(is_empty('0'))
# print(is_empty(0))

"""has_alpha Test Cases"""
# print(has_alpha("asd"))
# print(has_alpha("34-234"))
# print(has_alpha("asd"))
# print(has_alpha('09'))
# print(has_alpha('0'))
# print(has_alpha('asd ew0'))
# print(has_alpha('asdA13ew0'))
# print(has_alpha(0))


original_f = open('input.csv', 'r', newline='')
original_reader = csv.reader(original_f, delimiter=',', quotechar='"')

# with open('eggs.csv', newline='') as csvfile:
#   spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

empty_f = open('filter1/empty.csv', 'a')
empty_writer = csv.writer(empty_f, dialect='excel')

# empty_reader = csv.reader(empty_f)

with_alpha_f = open('filter1/with_alpha.csv', 'w')
# with_alpha_reader = csv.reader(with_alpha_f)

without_alpha_f = open('filter1/without_alpha.csv', 'w')
# without_alpha_reader = csv.reader(without_alpha_f)

# print(sum(1 for row in original_reader))

for row in original_reader:
    print(f"got: {row} : {len(row)}")
    print(type(row))
    print(len(row))
    # empty_writer.writerow(row)

    # empty_f.write(row,'\n')

    # empty_writer.writerow(row)

