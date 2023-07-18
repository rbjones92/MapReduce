# Robert Jones
# 7.17.23
# Reducer - Reduce VINs to make, model, and year

import sys

for line in sys.stdin:
    vin_dict = eval(line)

data = open('data.csv').readlines()
data_list = [line for line in data if line]
data_list = [line.split(",") for line in data_list]

for x in range(0,len(data_list)):
    vin = data_list[x][2]
    data_list[x][3] = vin_dict[vin][0]
    data_list[x][4] = vin_dict[vin][1]
    data_list[x][5] = vin_dict[vin][2]

data_list = [item for sublist in data_list for item in sublist]

print(data_list)
