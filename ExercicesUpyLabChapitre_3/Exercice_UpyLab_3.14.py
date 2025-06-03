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
Nb_essai = 1
print("Tirage :",tirage)
while Nb_essai <= 6:
    print("essai",Nb_essai)
    Nb_propose = int(input("Entrez votre nombre : "))
    if Nb_propose > tirage and Nb_essai < 6:
        print("Trop grand")
    if Nb_propose < tirage & Nb_essai < 6:
        print("Trop petit")
    if Nb_propose == tirage:
        print("Gagné en",Nb_essai,"essai(s) !")
        Nb_essai = 10
    Nb_essai +=1
if Nb_essai == 7 and Nb_propose != tirage:
    print("Perdu ! Le secret était",tirage)