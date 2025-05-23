"""
Exercice UpyLaB 3.5
Écrire un programme qui lit en entrée deux nombres entiers strictement positifs, et qui vérifie qu’aucun des deux n’est un diviseur de l’autre.
Si tel est bien le cas, le programme imprime True. Sinon, il imprime False.
"""
a = int(input("a ? "))
b = int(input("b ? "))
if a % b != 0 and b % a != 0:
    print("True")
else: 
    print("False")