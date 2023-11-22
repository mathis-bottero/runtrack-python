def calcul(nombre):
    if nombre > 0:
        return "positif"
    elif nombre < 0:
        return "négatif"
    else:
        return "nul"

resultat = calcul(6)
print(resultat)