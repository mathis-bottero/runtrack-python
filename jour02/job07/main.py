chaine = "abcdefghijklmnopqrstuvwxyz" * 10


nombre_total_caracteres = 50


chaine = "abcdefghijklmnopqrstuvwxyz"
n = 10

for i in range(1, n + 1):
    ligne = chaine[:i]
    print(ligne)