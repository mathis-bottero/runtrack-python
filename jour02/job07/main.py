chaine = "abcdefghijklmnopqrstuvwxyz" * 10


nombre_total_caracteres = 50


compteur_caracteres = 0


for i in range(1, 12, 2):
    espace = " " * ((11 - i) // 2)
    partie_chaine = chaine[compteur_caracteres:compteur_caracteres + i]
    ligne = espace + partie_chaine + espace
    print(ligne)
    

    compteur_caracteres += i


    if compteur_caracteres >= nombre_total_caracteres:
        break