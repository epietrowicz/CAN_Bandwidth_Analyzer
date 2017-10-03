import matplotlib.pyplot as plt
import numpy as np
import math
import collections
import datetime
from tkinter.filedialog import askopenfilename


dataArray = []
fileLength = 0
tempArray = []
identArray = []
timeArray = []
hexArray = []
temp = "00:00"
start = datetime.datetime.strptime(temp,"%M:%S")

#Open the MiniMon data change this value for file location
filename = askopenfilename()
with open(filename,"r") as file:
    for line in file:
        dataArray.append(line)
        fileLength = fileLength +1 
        
for i in range(7,fileLength):
    data = dataArray [i]

    for c in range(1,9):
        tempArray.append(data[c])
    for k in range(16,19):
        identArray.append(data[k])
        
    identStr = ''.join(identArray)
    timeStr = ''.join(tempArray)
    
    tempArray = []
    identArray = []
    timeArray.append(timeStr)
    hexArray.append(identStr)
    
overLoad = max(((item, hexArray.count(item)) for item in set(hexArray)), key=lambda a: a[1])[0]
print(overLoad)
    
for j in range(len(timeArray)):
    end = datetime.datetime.strptime(timeArray[j],"%H:%M:%S")
    delta = end - start
    secs = delta.total_seconds()
    timeArray[j] = secs

count = {x:timeArray.count(x) for x in timeArray}   #Count the number of times a number appears

lists = sorted(count.items())                       #Plot the data and calculate the percent of CAN used
x,y = zip(*lists)

y = tuple([z * 0.7265625 for z in y])

plt.plot(x,y)

plt.xlabel('Time(s)')
plt.ylabel('Percent CAN Usage(%)')
plt.title(filename)
plt.grid(True)
plt.ylim(0,100)
plt.xlim(0,max(x))

plt.show()
