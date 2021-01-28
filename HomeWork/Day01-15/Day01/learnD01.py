from turtle import *

'''   
turtle.pensize(4)
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()
'''

pensize(4)
colormode(255)
color((255, 155, 192), "pink")
setheading(-30)
begin_fill()
a = 0.4
for i in range(120):
    if 0 <= i < 30 or 60 <= i <90:
        a = a + 0.08
        # 向左转3度
        left(3)
        # 向前走
        forward(a)
    else:
        a = a - 0.08
        left(3)
        forward(a)
end_fill()
penup()
setheading(90)
forward(25)
setheading(0)
forward(10)
pendown()
pencolor(255, 155, 192)
setheading(10)
begin_fill()
circle(5)
color(160, 82, 45)
end_fill()
penup()
setheading(0)
forward(20)
pendown()