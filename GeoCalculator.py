'''This program calculates the area of a geometric shape'''
from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print ("Welcome to PiCal")

print ("%s/%s/%s %s:%s") % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to include the correct unit! \nExiting..."

option = raw_input("enter C for Circles or T for Triangle: ").upper()

if option == "C":
    radius = float(raw_input("Please enter the radius of the circle: "))
    area = pi * radius ** 2
    print "the pie is baking",
    sleep(1)
    print ".",
    sleep(1)
    print ".",
    sleep(1)
    print "."
    print ("Area: %.2f \n%s" % (area,hint))
elif option == "T":
    base = float(raw_input("Please enter the base of the triangle: "))
    height = float(raw_input("Please enter the height of the triangle: "))
    area = (base * height) / 2
    print "Uni Bi Tri",
    sleep(1)
    print ".",
    sleep(1)
    print ".",
    sleep(1)
    print "."
    print ("Area: %.2f \n%s" % (area,hint))
else:
    print ("Learn to read douche bag")
