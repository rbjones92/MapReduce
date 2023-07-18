# Robert Jones
# 7.17.23
# Mapper - Map 1 to "A" (accident)
import sys

data = sys.stdin.read()
data = eval(data)
data = [data[i:i+8] for i in range(0, len(data), 8)]

for x in range(len(data)):
    if data[x][1] == 'A':
        data[x].append(1)
    else:
        data[x].append(0)

data_list = [item for sublist in data for item in sublist]

print(data_list)
