"""
Suite de Fibonacci pour les n premiers termes
Va utiliser la boucle for pour construire la suite
"""
precedent = 0
successeur = 1
Nb_termes = int(input("Combien de termes dans le suite ? "))
print(precedent, end = " ")
print(successeur, end = " ")
for i in range(Nb_termes-2):
    precedent, successeur = successeur, precedent + successeur
    print(successeur, end = " ")
print()

"""
ou 

precedent = 0
successeur = 1
temporaire = 0
Nb_termes = int(input("Combien de termes dans le suite ? "))
print(precedent, end = " ")
print(successeur, end = " ")
for i in range(Nb_termes-2):
    #precedent, successeur = successeur, precedent + successeur
    temporaire = precedent
    precedent = successeur
    successeur = temporaire + precedent
    print(successeur, end = " ")
print()
"""