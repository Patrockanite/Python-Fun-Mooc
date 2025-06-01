"""
Exercice UpyLaB 3.11
Écrire un programme qui lit sur input une valeur naturelle n et qui affiche à l’écran un carré de n caractères X (majuscule) de côté.
"""
nb_x = int(input("Nb_x ? : "))
for i in range(nb_x):
    for j in range(nb_x):
        print("X",end="")
    print()