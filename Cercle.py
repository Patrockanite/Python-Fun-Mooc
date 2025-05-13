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

#lecture du rayon
rayon = float(input("Veuillez donner le rayon : "))
circ = 3.14 * 2 * rayon #calcul de la circonférence
aire = 3.14 * rayon ** 2 #calcul de l'aire du disque
#affichage des résultats
print("Circonférence :", circ)
print("Aire          :",aire)