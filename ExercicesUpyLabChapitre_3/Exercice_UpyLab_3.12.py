"""
Variante de l'exercice Exercice_UpyLab_3.11


"""
nb_X = int(input("Taille du côté : "))
for i in range(nb_X):  # ligne par ligne
    for j in range(i):  # imprime les espaces croissants
        print(" ", end="")
    for k in range(nb_X - i):  # imprime les X décroissants
        print("X", end="")
    print()  # retour à la ligne