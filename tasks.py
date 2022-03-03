#date (1)
from datetime import date, timedelta
past = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',past)


#date (2)
import datetime 
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('Yesterday: ',yesterday)
print('Today: ',today)
print('Tomorrow: ',tomorrow)


#date (3)
import datetime
current = datetime.datetime.today().replace(microsecond=0)
print(current)


#date (4)
from datetime import datetime, time
def diff(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.strptime('2000-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
print(diff(date2, date1), "seconds")


#math (1)
from math import pi
degree = float(input("Input degree: "))
radian = degree*(pi/180)
print("Output radian: ", radian)


#math (2)
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
height = float(input("Height: "))
S = ((base1+base2)/2)*height
print("Expected Output: ", S)
    

#math (3)
from math import tan, pi
number = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
s = int(number * (length ** 2) / (4 * tan(pi / number)))
print("The area of the polygon is: ", s)


#math (4)
a = float(input("Length of base: "))
b = float(input("Height of parallelogram: "))
s = float(a * b)
print("Expected Output: ", s)


#gen (1)
n = int(input())
for i in range (1, n+1) :
    print(i**2)
    

#gen (2)
n = int(input())
for i in range (0, n+1) :
    if (i%2==0) :
        if (i != 0):
            print(', ', end='')
        print(i, end='')
print()


#gen (3)
n = int(input())
for i in range (0, n+1) :
    if (i%12==0) :
        print(i)    


#gen (4)
a = int(input())
b = int(input())
for i in range (a, b+1) :
    print(i**2)


#gen (5)
n = int(input())
for i in range(n, -1, -1) :
    print(i)

    
#json
import json

with open('sample-data.json') as f:
    temp = json.load(f)

print(  'Interface Status\n' +
        '==============================================================================================\n' +
        'DN\t\t\t\t\t\tDescription\t\tSpeed\t\tMTU\n' +
        '-----------------------------------------------\t-----------------------\t---------------\t------')
for i in range(temp['imdata'].__len__()):
    print(  temp['imdata'][i]['l1PhysIf']['attributes']['dn'] + '\t' +
            temp['imdata'][i]['l1PhysIf']['attributes']['descr'] + '\t\t\t' +
            temp['imdata'][i]['l1PhysIf']['attributes']['speed'] + '\t\t' +
            temp['imdata'][i]['l1PhysIf']['attributes']['mtu'])
