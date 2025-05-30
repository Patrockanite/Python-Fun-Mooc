"""
Etoile à 5 branches avec la boucle for
"""
import turtle          # importation du module turtle
Nb_branches = 5
proposition = int(input("Combien de branches pour votre étoile ? "))
if proposition > Nb_branches: #Pour avoir au moins 5 branches
    Nb_branches = proposition
if Nb_branches % 2 == 0: #Pour n'avoir que des nombres impairs
    Nb_branches -=1
angle_interieur = (Nb_branches - 1)*180/Nb_branches
turtle.up()            # tant que la tortue est en mode “up”,
                       # son déplacement ne trace rien
turtle.shape('turtle') # change la forme de la tortue (en tortue)
turtle.goto(-80,0)     # la tortue se place en coordonnées (-80, 0)
                       # (-80 pour l’axe des "x" et 0 l’axe des "y")
turtle.color('blue')   # la tortue est bleue
turtle.down()          # tant que la tortue est “down”,
                       # elle tracera la ligne de ses déplacements
turtle.begin_fill()    # va remplir l’intérieur de ce qui est tracé entre
                       # maintenant et le turtle.end_fill() ultérieur
for i in range(Nb_branches):
    turtle.forward(300)    
    turtle.right(angle_interieur)      


turtle.end_fill()      # remplit ce qui a été tracé entre le begin_fill
                       # et cette instruction
turtle.hideturtle()    # cache la tortue
turtle.done()          # laisse l'utilisateur fermer la fenêtre