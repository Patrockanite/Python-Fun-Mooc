"""
Écrire un programme qui lit 3 nombres entiers, et qui, si au moins deux d’entre eux ont la même valeur, imprime cette valeur (le programme n’imprime rien dans le cas contraire).
"""
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
if a==b or a==c:
    print(a)
elif b==c:
    print(b)
