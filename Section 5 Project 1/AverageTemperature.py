import numpy as np
# Calculate Average Temperature

numDays = int(input("How many day's would you like to check for? "))
temperature = np.array([], dtype=int)

for i in range(1, numDays+1):
    weather = int(input(f"Day {i}'s high temp: "))
    temperature = np.append(temperature,[weather])
    
average = round(sum(temperature)/len(temperature),2)
daysAboveAverage = 0

for i in temperature:
    if i > average:
        daysAboveAverage += 1
        

print(f"Average = {average}")
print(f"{daysAboveAverage} day(s) above average")