"""
Exercice UpyLaB 3.7
Dans mon casino, ma roulette comporte 13 numéros de 0 à 12 comme montrés ci-dessous :

Le joueur a plusieurs types de paris possibles :

il peut choisir de parier sur le numéro sortant, et dans ce cas, s’il gagne, il remporte douze fois sa mise ;

il peut choisir de parier sur la parité du numéro sortant (pair ou impair), et dans ce cas, s’il gagne, il remporte deux fois sa mise ;

enfin, il peut choisir de parier sur la couleur du numéro sortant (rouge ou noir), et dans ce cas aussi, s’il gagne, il remporte deux fois sa mise.

Si le joueur perd son pari, il ne récupère pas sa mise.

Pour simplifier, on suppose que le numéro 0 n’est ni rouge ni noir, mais est pair. Pour simplifier encore, on suppose que le joueur mise systématiquement 10 euros.

Écrire un programme qui aide le croupier à déterminer la somme que le casino doit donner au joueur.

Le programme lira, dans l’ordre, deux nombres entiers en entrée : le pari du joueur (représenté par un nombre entre 0 et 16, voir description plus bas), et le numéro issu du tirage (nombre entre 0 et 12). Le programme affichera alors le montant gagné par le joueur.

Entrées pour le pari du joueur :

nombre entre 0 et 12 : le joueur parie sur le numéro correspondant

13 : le joueur parie sur pair

14 : le joueur parie sur impair

15 : le joueur parie sur la couleur rouge

16 : le joueur parie sur la couleur noire.
"""


mise = 10
choix = int(input("Choix : "))
tirage = int(input("tirage ? "))


if choix >=0 and choix < 13:
    if choix == tirage:
        print(mise*12)
    else: print(0)

if choix == 13:
    if tirage % 2 == 0:
        print(mise*2)
    else:
        print(0)
if choix == 14:
    if tirage % 2 != 0:
        print(mise*2)
    else: print(0)
if choix == 15:
    if (tirage == 3 or tirage == 9 or tirage == 12 or tirage == 5 or tirage == 1 or tirage == 7):
        print(mise*2)
    else: print(0)
if choix == 16:
    if (tirage == 6 or tirage == 2 or tirage == 8 or tirage == 11 or tirage == 4 or tirage == 10):
        print(mise*2)
    else: print(0)



