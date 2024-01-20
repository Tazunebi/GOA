from turtle import*


#we want to paint a house

#step1: draw a square
speed(30)
width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(180,180)
pendown()

color("brown")

left(30)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)





penup()
goto(+20, +180)
pendown()

color("brown")

right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(340, 340)
pendown()

color("yellow")
begin_fill()
circle(50)
end_fill()

penup()
goto(-200, 0)
pendown()

color("saddle brown")       
begin_fill() 
right(90)
forward(220)
right(90)
forward(50)
right (90)
forward(220)
right(90)
forward(50)
end_fill()

penup()
goto(-180, 260)
pendown()


color("green")
begin_fill()
circle(70)
end_fill()

penup()
goto(-500, 0)
pendown()

color("green")
width(10)
right(180)
forward(1000)


exitonclick()
