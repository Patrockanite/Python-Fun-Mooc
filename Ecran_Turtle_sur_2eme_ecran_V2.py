"""
    Version de Ecran Turtle appelable depuis un autre fichier *.py
"""
#Ecran_Turtle_sur_2eme_ecran_V2

import turtle

def init_ecran_turtle_sur_deuxieme_ecran(x_pos=2020, y_pos=100, width=700, height=700):
    screen = turtle.Screen()
    root = turtle.getcanvas().winfo_toplevel()
    geometry_string = f"{width}x{height}+{x_pos}+{y_pos}"
    root.geometry(geometry_string)
    return screen

"""Code à ajouter dans le fichier principal
# main.py
import turtle
from ecran_turtle import init_ecran_turtle_sur_deuxieme_ecran

# Initialise l’écran sur le deuxième écran
screen = init_ecran_turtle_sur_deuxieme_ecran()

# Tracé Turtle
turtle.circle(100)

turtle.done()"""
