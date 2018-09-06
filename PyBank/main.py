import os
import csv
csvpath = os.path.join("..", 'PyBank', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    row_count = (sum(1 for row in csvreader) - 1)
    print(row_count)

import os
import csv
csvpath = os.path.join("..", 'PyBank', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header_row = next(csvreader)
    print(header_row)
    total = 0
    for row in csvreader:
        total = sum(int(row[1]))
        print(total)

import os
import csv
csvpath = os.path.join("..", 'PyBank', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header_row = next(csvreader)
    print(header_row)
    #average = 0
    for row in csvreader:
        average = (mean(1 for row in csvreader) - 1)
        print(average)

import os
import csv
csvpath = os.path.join("..", 'PyBank', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header_row = next(csvreader)
    print(header_row)

    max_profit = 0
    min_profit = 0

   for row in csvreader:
       max_profit = max(int(row[1]))
       min_profit = min(int(row[1]))
   print(max_profit)
   print(min_profit)