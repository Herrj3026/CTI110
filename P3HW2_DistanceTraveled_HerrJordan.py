#
# A program to do a basic calcuation of how far you travled
# 6/22/2021
# CTI-110 P3HW2 - DistanceTraveled
# Jordan Herr
#


#section for the inputs
car_speed = float(input("Please enter car speed: "))
time_travled = float(input("Please enter distance travled: "))

#math section for the calculations
dis_travled = car_speed * time_travled

if time_travled > 0:
    print()#white space to make it neat
    print("Speed entered:", car_speed)
    print("Time entered:", time_travled)
    print()#white space to make it neat
    print("Distance Travled", dis_travled)
elif time_travled <= 0:

    time_travled = 1

    print("Error!!! Time must be greater than 0!!!")
    print()#white space to make it neat
    print("Speed entered:", car_speed)
    print("Time:", time_travled)
    print()#white space to make it neat
    print("Distance Travled", dis_travled)
