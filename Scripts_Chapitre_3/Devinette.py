"""
Jeu de devinettes version 1
Auteur : Patrockanite
Date : 23 mai 2025
(c'est pour l'exercice)
"""
import random
secret = random.randint(0,5)
if int(input("Entrez votre proposition : ")) == secret:
    print("Gagné !")
else:
    print("Perdu ! La valeur était",secret)
print("Au revoir !")
    