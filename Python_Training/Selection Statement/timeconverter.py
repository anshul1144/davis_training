# program to input time in seconds and convert it to hours, minutes and seconds
# taking input from the user

seconds = int(input("Enter time in seconds: "))
# initialize hours and minutes 
hour= 0
minute = 0
# calculating no. of hours in given seconds
if seconds >= 3600:
    hour = seconds // 3600
    seconds = seconds % 3600
# calculating no. of minutes in given seconds
if seconds >= 60:
    minute = seconds // 60
    seconds = seconds % 60
# printing the result
print("Time :", hour, "hour", minute, "minute", seconds, "second")

#...................................................

""" Output:
Enter time in seconds: 3665
Time : 1 hour 1 minute 5 second
"""