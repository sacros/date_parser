#!/usr/bin/env python3
import csv
import re

def is_empty(inp):
    return True if inp in ('', 0, '0', '-', None) else False


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

empty_f = open('filter1/empty.csv', 'w+')
empty_writer = csv.writer(empty_f, dialect='excel')

with_alpha_f = open('filter1/with_alpha.csv', 'w+')
with_alpha_writer = csv.writer(with_alpha_f, dialect='excel')

without_alpha_f = open('filter1/without_alpha.csv', 'w+')
without_alpha_writer = csv.writer(without_alpha_f, dialect='excel')

listfile = open('dates', 'w+')


count = 0
dates = []

for row in original_reader:
    count += 1
    if count == 1:
      continue  
    # listfile.write(row[1]+'\n')
    dates.append(row[1])

    print(f'processing row {count}')
    # for index, cell in enumerate(row):
    #   row[index] = cell.replace("\n", "$")

    if is_empty(row[1]):
        empty_writer.writerow(row)
        # print(f'setting row#{count}, {row} to empty')        
    elif has_alpha(row[1]):
        with_alpha_writer.writerow(row)
        # print(f'setting row#{count}, {row} to with_alpha')        
    else:
        without_alpha_writer.writerow(row)
        # print(f'setting row#{count}, {row} to without_alpha')        
