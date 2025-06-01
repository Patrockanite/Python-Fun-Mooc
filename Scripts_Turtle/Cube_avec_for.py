"""
    Faire un cube en perspective comme dans Cube_colore.py mais sans couleur avec des boucles for"""
import turtle

angle = 180 - 60 #soit 120° - J'aurais pu mettre 120 mais c'est pour la compréhension
for i in range(3):  # à chaque itération, trace un losange
    turtle.left(angle) #on peut in verser la rotation avec la ligne 10 : turtle.right(angle)
    for j in range(4): # à chaque itération, trace un segment
        turtle.forward(150)
        turtle.right(angle) # si inversion turtle.left(angle)
        angle = 180 - angle #permet d'avoir une fois sur deux un angle à 120° et un angle à 60°
 
turtle.hideturtle()
turtle.mainloop()