"""
Exercice UpyLaB 3.13 

Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat.
La première donnée lue ne fait pas partie des valeurs à sommer. Elle détermine si la liste contient un nombre déterminé à l’avance de valeurs à lire ou non :
si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs à lire et à sommer ;
si elle est égale à -1, cela signifie qu’elle est suivie d’une liste de données à lire qui sera terminée par le caractère "F" signifiant que la liste est terminée.
"""
Nb_donnees = int(input("Nombre de données ? : "))
somme = 0
if Nb_donnees > 0:
    for i in range(Nb_donnees):
        terme = int(input("Entrer le nombre : "))
        somme = somme + terme
    print("somme =",somme)
if Nb_donnees == -1:
    terme = 0
    while terme != 'F':
        terme = input("Entrer le nombre : ")
        if terme != 'F':
            terme = int(terme)
            somme = somme + terme
    print("somme =",somme)
if Nb_donnees == 0:
    print(0)