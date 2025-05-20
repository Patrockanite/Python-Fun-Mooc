"""Auteur: Thierry Massart
   Date : 5 décembre 2017
   But du programme : calcule les ingrédients nécessaires
   pour préparer de la mousse au chocolat pour n personnes
   Entrée: n (nombre de personnes)
   Sorties: nombre d'oeufs,
            quantité en gramme de chocolat,
            nombre de sachets de sucre vanillé
"""
n = int(input("nombre de personnes : "))            # entrée: nombre de personnes
oeufs = int(3 * n / 4)                            # nombre d’oeufs nécessaires
chocolat = int(100 * n / 4)                       # quantité de chocolat nécessaire
sucre_vanille = max(int(n / 4), 1)                # quantité de sucre nécessaire
print("nombre d'oeufs : ", oeufs)                   # affiche les résultats
print("quantité de chocolat (g) : ", chocolat)
print("quantité de sucre_vanillé : ", sucre_vanille)