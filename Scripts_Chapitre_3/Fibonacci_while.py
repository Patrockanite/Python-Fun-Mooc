"""
Fibonacci avec boucle while
"""
n = int(input("Afficher les termes de la suite de Fibonacci inférieurs à : "))

a, b = 0, 1  # Termes initiaux

while a < n:
    print(a, end=" ")
    a, b = b, a + b

print()  # Pour retour à la ligne
