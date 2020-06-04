def calcAngle(hour,minute): 
    # validating the inputs here
    if (hour < 0 or minute < 0 or hour > 12 or minute > 60): print('Wrong input') 
    if (hour == 12): hour = 0
    if (minute == 60): minute = 0
    # Calculating the angles moved by hour and minute hands with reference to 12:00 
    hour_angle, minute_angle = 0.5 * (hour * 60 + minute), 6 * minute  
    # finding the difference between two angles 
    abs_angle = abs(hour_angle - minute_angle) 
    # Returning the smaller angle of two possible angles (min or max will not make much diff or no diff)
    angle = min(360 - abs_angle, abs_angle) 
    return angle 

# river program   
hour = 6
minute = 15
print('Angle ', calcAngle(hour,minute))