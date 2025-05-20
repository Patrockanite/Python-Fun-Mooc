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
"""