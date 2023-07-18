# Robert Jones
# 7.17.23
# Mapper - Map VINs to make, model, and year

import sys

vin_dict = {}
for line in sys.stdin:
    make = line.split(',')[3]
    model = line.split(',')[4]
    year = line.split(',')[5]
    if make and model and year:
        vin_dict[line.split(',')[2]] = make,model,year

print(vin_dict)