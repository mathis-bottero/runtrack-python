def nombre_multiples_de_3(list):
    count = 0
    for nombre in list:
        if nombre % 3 == 0:
            count += 1
    return count

L = [8, 24, 48, 2, 16]
resultat = nombre_multiples_de_3(L)
print(resultat)