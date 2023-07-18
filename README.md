# MapReduce

## Summary
Utilize MapReduce to find summary statistics for car accident data

## Description
MapReduce csv data to find summary counts of accident data per car 

## Technologies
- Python 3.11
- VS Code

## Local Execution
View Data
![Alt Text](screenshots/step_0.JPG?raw=true "load data")

MAP VIN to make,model,year
![Alt Text](screenshots/step_1.JPG?raw=true "map 1")

REDUCE VIN to make,model,year
![Alt Text](screenshots/step_2.JPG?raw=true "reduce 1")

MAP Accidents as 1
![Alt Text](screenshots/step_3.JPG?raw=true "map 2")

REDUCE Sum count of accidents and group by VIN 
![Alt Text](screenshots/step_4.JPG?raw=true "reduce 2")
