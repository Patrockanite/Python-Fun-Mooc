"""
Exercice UpyLaB 3.14
Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret) compris entre 0 et 100, bornes incluses. Ensuite, le joueur doit deviner ce nombre en utilisant le moins d’essais possible.

À chaque tour, le joueur est invité à proposer un nombre et le programme doit donner une réponse parmi les suivantes :
« Trop grand » : si le nombre secret est plus petit que la proposition et qu’on n’est pas au maximum d’essais
« Trop petit » : si le nombre secret est plus grand que la proposition et qu’on n’est pas au maximum d’essais
« Gagné en n essai(s) ! » : si le nombre secret est trouvé
« Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret.
"""
import random

#tirage = random.randint(0,100)
tirage = 42
essai = 1
print("Tirage :",tirage)
while essai <= 6:
    print("essai",essai)
    Nb_propose = int(input("Entrez votre nombre : "))
    if Nb_propose > tirage and essai < 6:
        print("Trop grand")
    if Nb_propose < tirage & essai < 6:
        print("Trop petit")
    if Nb_propose == tirage:
        print("Gagné en",essai,"essai(s) !")
        essai = 10
    essai +=1
if essai == 7 and Nb_propose != tirage:
    print("Perdu ! Le secret était",tirage)