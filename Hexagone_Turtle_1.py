"""
    Essai1 de dessin d'un hexagone sans utiliser la trigonométrie
"""
import turtle
turtle.color("green")
turtle.up()
turtle.goto(100,0)
turtle.down()
turtle.begin_fill()
turtle.left(120)
turtle.forward(100)
#turtle.left(60)
#turtle.forward(100)
#turtle.left(60)
#turtle.forward(100)
#turtle.left(60)
#turtle.forward(100)
#turtle.left(60)
#turtle.forward(100)
for i in range(4):
    turtle.left(60)
    turtle.forward(100)
turtle.end_fill()
turtle.hideturtle()
turtle.mainloop()