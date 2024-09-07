"""
QUESTION :-
Create a time (format: 00:hours and 00:minutes), 
After adding some more minutes, find out the updated time 
eg :- Time - 12:hours 40:minutes
      Adding 30 minutes
      Updated time - 1:hour 10:minutes

WORKING :-
First add hours and minutes, then program will show the time accordingly.
Afterr that,
Add more minutes and get the updated time in the output

"""

h = int(input("Enter hour: "))
m = int(input("Enter minutes: "))

print("The previous time is {}:hours and {}:min".format(h, m))

addMin = int(input("Enter more minutes: "))

while(addMin>60):
    addMin = addMin-60
    h=h+1

if(h>12):
    h=h-12
    
m=m+addMin

print("The updated time is {}:hours and {}:min".format(h, m))
