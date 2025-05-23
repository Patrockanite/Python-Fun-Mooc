"""
Exercice UpyLaB 3.8
Les cinq polyèdres réguliers de Platon sont représentés ci-dessous, avec la formule de leur volume.

Source des images de polyèdres : Vikidia, l’encyclopédie pour les jeunes, qui explique aux enfants et à ceux qui veulent une présentation simple d'un sujet (https://fr.vikidia.org/wiki/Polyèdre).  
"""
"""
Écrire un programme qui lit :

la première lettre en majuscule du nom du polyèdre ("T", "C", "O", "D" ou "I"),

la longueur de l’arête du polyèdre,

et qui imprime le volume du polyèdre correspondant.

Si la lettre lue ne fait pas partie des cinq initiales, le programme imprime le message "Polyèdre non connu".
"""
import math

polyedre = input("lettre ? ")
longueur_arrete = float(input("Longueur arrête ? "))
if polyedre == 'T':
    print(longueur_arrete**3*(math.sqrt(2)/12))
elif polyedre == 'C':
    print(longueur_arrete**3)
elif polyedre == 'O':
    print(longueur_arrete**3*(math.sqrt(2)/3))
elif polyedre == 'D':
    print(((15+7*math.sqrt(5))/4)*longueur_arrete**3)
elif polyedre == 'I':
    print((5*(3+math.sqrt(5))/12)*longueur_arrete**3)
else:
    print("Polyèdre non connu")