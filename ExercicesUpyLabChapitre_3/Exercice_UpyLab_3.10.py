"""
Exercice UpyLaB 3.10
Écrire un programme qui calcule la taille moyenne (en nombre de salariés) des Petites et Moyennes Entreprises de la région.

Les tailles seront données en entrée, chacune sur sa propre ligne, et la fin des données sera signalée par la valeur sentinelle -1. Cette valeur n’est pas à comptabiliser pour le calcul de la moyenne, mais indique que l’ensemble des valeurs a été donné.

Après l’entrée de cette valeur sentinelle -1, le programme affiche la valeur de la moyenne arithmétique calculée (de type float).

On suppose que la suite des tailles contient toujours au moins un élément avant la valeur sentinelle -1, et que toutes ces valeurs sont positives ou nulles.
"""
Nb_entree = 0
Nb_salaries = 0
Nouvelle_entree = 0
while Nouvelle_entree != -1:
    Nouvelle_entree = int(input("Nombre de salariés ? : "))
    if Nouvelle_entree != -1:
        Nb_salaries = Nb_salaries + Nouvelle_entree
        Nb_entree = Nb_entree + 1
print("La moyenne est : ", Nb_salaries/Nb_entree)