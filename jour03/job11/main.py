def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        resultat = ""

        if heures > 0:
            resultat += f"{heures} heure{'s' if heures > 1 else ''}"
        
        if heures > 0 and minutes_restantes > 0:
            resultat += " et "
        
        if minutes_restantes > 0:
            resultat += f"{minutes_restantes} minute{'s' if minutes_restantes > 1 else ''}"

        print(resultat or "0 minute") 

    else:
        print("Veuillez entrer un nombre entier de minutes positif.")

time_to_text(350)