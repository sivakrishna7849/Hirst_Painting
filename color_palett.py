# import colorgram
# colors=colorgram.extract('color.jpg',50)
# rgb_colors=[]
# for i in colors:
#     r=i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb_colors.append((r,g,b))
import turtle as t
import random
tim=t.Turtle()
tim.speed("fastest")
t.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
color_list=[(246, 243, 239), (247, 241, 244), (202, 166, 109), (240, 246, 241), (152, 73, 47), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212), (109, 123, 149), (173, 198, 205), (105, 136, 143), (72, 64, 55)]
for i in range(10):
    placex=tim.xcor()
    placey=tim.ycor()
    tim.pendown()
    for j in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.setx(placex)
    placey+=50
    tim.sety(placey)
screen=t.Screen()
screen.exitonclick()