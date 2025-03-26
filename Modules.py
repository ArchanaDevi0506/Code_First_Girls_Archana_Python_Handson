#Modules - these allow you to use other People's Code
import math #includes lots of mathematical functions
import datetime  #This is a module that allows you to work with dates and times
import timeit    #This is a module that allows you to measure the time it takes to execute a code snippet
currentdate = datetime.datetime.now()
print(currentdate)
newdate = datetime.date(2024, 11, 17)
print(newdate)

#we can format the date howerver we would like
print(newdate.strftime("%A %d %B %Y"))
print(math.sqrt(16))