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

secret = random.randint(0, 100)
#secret = 7  # Pour les tests
NB_ESSAIS_MAX = 6
essais = 0
trouve = False

while essais < NB_ESSAIS_MAX and not trouve:
    Nb_propose = int(input("Entrez votre nombre : "))
    essais += 1
    if Nb_propose > secret and essais < NB_ESSAIS_MAX:
        print("Trop grand")
    elif Nb_propose < secret and essais < NB_ESSAIS_MAX:
        print("Trop petit")
    elif Nb_propose == secret:
        print("Gagné en", essais, "essai(s) !")
        trouve = True

if not trouve:
    print("Perdu ! Le secret était", secret)
