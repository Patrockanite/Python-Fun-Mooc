"""
    Résolution d'une équation du second degré ax^2+bx+c = 0

    où a, b et c sont des valeurs réelles, pour savoir si cette équation a deux, une ou aucune racines réelles, il faut calculer le discriminant delta qui vaut :
    delta = b^2-4ac
    Si la valeur de delta est strictement positive, l’équation a deux racines réelles :
    
    x_1 = (-b-sqrt(delta))/2a

    x_2 = (-b+sqrt(delta))/2a

    Si la valeur de delta est égale à 0, l’équation a une racine :
    x = -b/2a

Si la valeur de delta est strictement négative, l’équation n’a pas de racine réelle.
méthode : il faut calculer le discriminant : Delta = b^2-4ac
Donc pour -x^2+x+6=0 ==> a=-1 , b=1 et c=6 ==> -1*x^2 + 1*x + 6 = 0
"""
import math

print("Résolution d'une équation de second degré ax^2 + bx + c = 0")
a = float(input("Pour ax^2, valeur de a = "))
b = float(input("Pour bx, valeur de b = "))
c = float(input("Valeur de c = "))
# Calcul du discriminant
delta = b**2-4*a*c
print("Discriminant delta =",delta)
if delta < 0:
    print("Il n'y a pas de solution dans R")
elif delta == 0:
    print("Il n'existe qu'une solution : x =",-1*b/(2*a))
else:
    print("Il existe 2 solutions à l'équation :")
    print("x1 =",(-1*b-math.sqrt(delta))/(2*a))
    print("x2 =",(-1*b+math.sqrt(delta))/(2*a))
