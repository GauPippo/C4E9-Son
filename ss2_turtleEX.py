from turtle import *
import turtle

colormode()
shape("turtle")
speed(0)

colors = ["red","blue","brown","yellow","grey"]

for n in range(3, 8):
    for i in range(n):
        forward(100)
        left(360/n)
    color(colors[n-3])
