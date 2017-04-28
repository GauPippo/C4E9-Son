#1.
'''
- How to check a variable's type?
    type()

- Three difference examples of invalid name.
    1992abc = 10
    abc$ = "name"
    True = 'hahaha'
'''

#2.
from math import *
from turtle import *
import turtle

##pi = 3.14

##radius = int(input("Radius?"))
##print ("Area =", radius * pi)
##print ("hihihi")

###3.
##
##doC = int(input("Enter the temperature in Celsius?"))
##doF = 9.0/5.0 * doC + 32
##print(doC, "C = ", doF, "F")

# TURTLE EXERCISE

shape("turtle")
speed(-1)

##for n in range(3, 5):
##    for i in range(n):
##        forward(100)
##        left(360/n)
    
size=36
bgcolor("black")
pensize(5)
pencolor("white")
speed(400)
for i in range(size):
    rt(90);pencolor("pink")
    circle(60,360)
    lt(120);pencolor("yellow")
    circle(90,360)
    lt(120);pencolor("green")
    circle(120,360)
    circle(150)


print("Toi da sua file nay")
