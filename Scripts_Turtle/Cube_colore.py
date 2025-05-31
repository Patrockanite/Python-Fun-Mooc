"""
    Pour essayer de faire un cube en perspective avec des couleurs comme dans l'exemple de Fun Mooc
"""
import turtle
turtle.color("black")
turtle.begin_fill()
turtle.forward(150)
turtle.right(120)
turtle.forward(150)
turtle.right(60)
turtle.forward(150)
turtle.right(120)
turtle.forward(150)
turtle.end_fill()


turtle.color("blue")
turtle.begin_fill()

turtle.right(60)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(60)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.end_fill()


turtle.color("red")
turtle.begin_fill()

turtle.right(60)
turtle.forward(150)
turtle.right(120)
turtle.forward(150)
turtle.right(60)
turtle.forward(150)
turtle.right(120)
turtle.forward(150)
turtle.end_fill()


turtle.hideturtle()
turtle.mainloop()