def recuperation(liste):
    valeur_max = None
    valeur_min = None

    for nombre in liste:
        if valeur_max is None or nombre > valeur_max:
            valeur_max = nombre

        if valeur_min is None or nombre < valeur_min:
            valeur_min = nombre

    return valeur_max, valeur_min

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
max_val, min_val = recuperation(L)

print("La valeur max est :", max_val)
print("La valeur min est :", min_val)



