"""
    Essai d'hexagone Turtle avec le trigonométrie On modifiera pour un polygone où on entrera le nombre de côtés
"""
import turtle
import math

"""# Crée l'écran turtle
screen = turtle.Screen()

# Taille et position
width = 600
height = 600
x_pos = 1920 + 100  # Pour 2e écran à droite de 1920px
y_pos = 100

# Récupère la fenêtre Tk associée à Turtle
root = turtle.getcanvas().winfo_toplevel()

# Applique la géométrie
geometry_string = f"{width}x{height}+{x_pos}+{y_pos}"
root.geometry(geometry_string)"""

from Ecran_Turtle_sur_2eme_ecran_V2 import init_ecran_turtle_sur_deuxieme_ecran

# Initialise l’écran sur le deuxième écran
screen = init_ecran_turtle_sur_deuxieme_ecran()
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