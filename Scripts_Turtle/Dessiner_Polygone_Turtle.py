"""
Dessiner un Polygone à au moins 3 côtés vaec Turtle
"""
import math
import turtle
from Ecran_Turtle_sur_2eme_ecran_V2 import init_ecran_turtle_sur_deuxieme_ecran

#entrée du nombre de côtés et initialisation de l'angle
Nb_de_cotes = int(input("Nombre de côtés du polygone ? "))
if Nb_de_cotes<3:
    Nb_de_cotes=3
    print("On retiendra un triangle")
angle = 360//Nb_de_cotes
rayon = int(input("Rayon du cercle où est inscrit le polygone ? "))
#print("angle :",angle)
# Initialise l’écran sur le deuxième écran
screen = init_ecran_turtle_sur_deuxieme_ecran()

#dessine le polygone
turtle.color("green")
turtle.up()
turtle.goto(rayon*math.cos(math.radians(0)),rayon*math.sin(math.radians(0)))
turtle.down()
turtle.begin_fill()
for i in range(1,Nb_de_cotes+1):
    turtle.goto(rayon*math.cos(math.radians(angle*i)),rayon*math.sin(math.radians(angle*i)))
turtle.end_fill()
turtle.hideturtle()
turtle.mainloop()