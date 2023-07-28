# Robert Jones
# 7.17.23
# Mapper - Map 1 to "A" (accident)

import sys

data = sys.stdin.read()
data = eval(data)
data = [data[i:i+9] for i in range(0, len(data), 9)]

output_dict = {}
for x in range(len(data)):
    if data[x][8] == 1:
        key = (data[x][3], data[x][5])
        if key in output_dict:
            output_dict[key] += 1
        else:
            output_dict[key] = data[x][8]

print(output_dict)