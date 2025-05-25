"""
Calcul du PGCD : Plus Grand Commun Diviseur
Le plus grand diviseur (pgcd) des deux nombres est le nombre d qui est :

un diviseur entier à la fois de x et de y, c’est-à-dire que
x divisé par d donne un nombre entier,

et de même pour y divisé par d,

et de plus tel qu’il n’existe pas d’autre entier strictement plus grand que d
également diviseur entier à la fois de x et de y.

Ainsi on peut vérifier que 12 est le plus grand commun diviseur de 132 et 36.
"""
x = int(input("x = "))
y = int(input("y = "))
while y > 0:
    x, y = y, x % y
    print(x, y)
print("pgcd = ", x)
"""
Le script met directement en application deux propriétés mathématiques du pgcd, soit :

Si x est positif et y strictement positif : pgcd(x, y) est équivalent à pgcd(y, x % y)
Par exemple 132 % 36 vaut 24 et donc pgcd(132, 36) vaut pgcd(36, 24)
ce qui est intéressant car y et x % y seront plus petits que x et y.
pgcd(x, 0) vaut x.
"""