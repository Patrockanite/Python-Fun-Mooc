"""
CONJECTURE DE SYRACUSE :
La suite de Collatz pour un nombre entier n strictement positif est définie comme suit :
la première valeur de la suite est le nombre n lui-même,
si n est pair la valeur suivante sera n divisé par 2,
sinon la valeur suivante est 3n + 1 (n multiplié par 3 auquel on rajoute 1).
En répétant l’opération, on obtient une suite d’entiers positifs dont chacun ne dépend que de son prédécesseur.
Par exemple, à partir de 14, on construit la suite des nombres : 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2…
C’est ce qu’on appelle la suite de Collatz ou suite de Syracuse du nombre 14.
Après que le nombre 1 a été atteint, la suite des valeurs (1,4,2,1,4,2…) se répète indéfiniment en un cycle de longueur 3, appelé cycle trivial.
"""
Nb = int(input("Entrez un nombre entier : "))

while Nb != 1:
    if Nb % 2 == 0:
        Nb = Nb//2
        if Nb ==1: # Pour ne pas avoir la flèche à la fin
            print(Nb)
        else:
            print(Nb,end = "→") # flèche = alt + 26 
    else:
        Nb = 3*Nb+1
        if Nb ==1: # Pour ne pas avoir la flèche à la fin
            print(Nb)
        else:
            print(Nb,end = "→")        
print('')
print("On est au bout","\n") 