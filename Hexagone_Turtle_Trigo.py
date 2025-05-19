"""
    Essai d'hexagone Turtle avec le trigonométrie On modifiera pour un polygone où on entrera le nombre de côtés
"""
import turtle
import math
#entrée du rayon
rayon = int(input("Rayon de l'hexagone ? "))
angle = 60 #Angle du polygone soit pour 6 côtés 360/6 = 60
turtle.color("green")
turtle.up()
#turtle.goto(0,-100)
#turtle.down()
#turtle.circle(100)
#turtle.up()
#turtle.goto(0,0)
turtle.goto(rayon*math.cos(math.radians(0)),rayon*math.sin(math.radians(0)))
turtle.down()
turtle.begin_fill()
for i in range(1,7):
    turtle.goto(rayon*math.cos(math.radians(angle*i)),rayon*math.sin(math.radians(angle*i)))
turtle.end_fill()
turtle.hideturtle()





turtle.mainloop()