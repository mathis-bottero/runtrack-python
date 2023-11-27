def distance(marches, hauteur):
    nombre_de_marches = marches * 2
    distance_par_marche = hauteur / 100

    distance_totale = nombre_de_marches * distance_par_marche * 7

    return distance_totale

nombre_de_marches = 20
hauteur_marche = 25
distance_parcourue = distance(nombre_de_marches, hauteur_marche)

print(f"Pour {nombre_de_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_parcourue:.2f} m par semaine.")