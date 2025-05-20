""" Auteur: Sébastien Hoarau
    date : juin 2018
    But du programme :
    Le programme suivant calcule la circonférence
    et l’aire d’un disque dont le rayon est donné
    en input
    Entrée: rayon : le rayon du disque
    Sorties: la circonférence du disque
             l'aire du disque
"""
from math import pi

#lecture du rayon
rayon = float(input("Veuillez donner le rayon : "))
circ = pi * 2 * rayon #calcul de la circonférence
aire = pi * rayon ** 2 #calcul de l'aire du disque
#affichage des résultats
print("Circonférence :", circ)
print("Aire          :",aire)