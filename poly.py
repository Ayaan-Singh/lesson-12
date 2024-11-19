import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
numsides = 10
side_length = 80
angle = 360 / numsides
for i in range (numsides):
   polygon.forward(side_length)
   polygon.right (angle)
turtle.done()