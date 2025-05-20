"""
    Années bissextiles : Première approximation, où nous considérons que nous avons une année bissextile tout les quatre ans et que l’année bissextile est celle dont la valeur est divisible par 4 (par exemple 2020 est bissextile).
"""
annee_a_tester = int(input("Entrez l'année à tester : "))
# 1ère version de test
"""if annee_a_tester % 4 == 0:
    print("l'année", annee_a_tester, "est bissextile")
else:
    print("l'année", annee_a_tester, "n'est pas bissextile")"""

#2 ème version de test
"""
    Depuis l’ajustement du calendrier grégorien, l’année sera bissextile :
    si l’année est divisible par 400 ou
    si l’année est divisible par 4 mais non divisible par 100.    
    Sinon, l’année n’est pas bissextile.
"""
if annee_a_tester % 400 == 0:
    print("l'année", annee_a_tester, "est bissextile")
elif annee_a_tester % 100 == 0:
    print("l'année", annee_a_tester, "n'est pas bissextile")
elif annee_a_tester % 4 == 0:
    print("l'année", annee_a_tester, "est bissextile")
else:
    print("l'année", annee_a_tester, "n'est pas bissextile")