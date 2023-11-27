def calculate(list):
    prod = 1
    for value in list:
        if 25 <= value <= 90:
            prod *= value
    return prod

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
resultat = calculate(L)
print("Le produit des valeurs de L comprises entre [25 et 90] est :",resultat)