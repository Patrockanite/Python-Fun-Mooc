"""
    Faire un cube en perspective comme dans Cube_colore.py mais sans couleur avec des boucles for"""
import turtle

angle = 120

for i in range(4):
    turtle.forward(150)
    turtle.right(angle)
    angle = 180 - angle
 
turtle.left(angle)
for i in range(4):
    turtle.forward(150)
    turtle.right(angle)
    angle = 180 - angle

#turtle.color("blue")
#turtle.begin_fill()

turtle.left(angle)
for i in range(3):
    turtle.forward(150)
    turtle.right(angle)
    angle = 180 - angle

turtle.hideturtle()
turtle.mainloop()