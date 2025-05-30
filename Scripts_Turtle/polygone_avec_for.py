"""
DESSIN D’UN CARRÉ, D’UN POLYGONE RÉGULIER AVEC TURTLE
"""
import turtle

#Nombre de côtés
Nb_cotes = int(input("Entrez le nombre de côtés : "))
for i in range(Nb_cotes):
    turtle.forward(100)
    turtle.left(360//Nb_cotes) #pour dessiner un polygone à n côtés (par exemple n = 5), l’angle intérieur entre deux côtés est de 360°/n. Si n vaut 5 cela donne donc 72°.
turtle.done()
