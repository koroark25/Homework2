#katherine o'roark 
#1
def print_name(name):
    print("The name is", name)

print_name("Katherine")

#2
import math
def ninety(a,b,c):
    #(a+b+c+d)/4 = 90
    #multiply by 4 on both sides
    #a+b+c+d = 360
    #sutract both sides by a, b, and c
    #d = 360-a-b-c
    d = 360-a-b-c
    return d

print(ninety(40,8,390))

#3
def miles_per_hour(miles,hours,minutes,seconds):
    #we must get a total amount of hours, including the minutes and seconds
    #to get this, we must convert minutes to hours and seconds to hours
    #minutes/60
    #seconds/3600
    #then, we add that value to the existing hours
    tot_hour = hours + (minutes/60) + (seconds/3600)
    return miles/tot_hour

print(miles_per_hour(20,2,21,16))

#4
def greeting(name):
    if name == "Chris":
        print("Hello, Chris.")
    else:
        print("Goodbye,", name + ".")

greeting("Chris")
greeting("Jake")

#5
def convert_temperature(temp,units):
    if units == "celsius":
        return temp*1.8 + 32
    elif units == "fahrenheit":
        return (temp-32)/1.8
    else:
        return "please enter a valid unit"
print(convert_temperature(12,'celsius'))
print(convert_temperature(45,'fahrenheit'))
print(convert_temperature(273.15,'kelvin'))

#6
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'
print(calculate_grade(98))
print(calculate_grade(87))
print(calculate_grade(73))
print(calculate_grade(66))
print(calculate_grade(50))
