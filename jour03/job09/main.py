def moyenne(note1, note2, note3):
    moyenne_etudiant = (note1 + note2 + note3) / 3
    return moyenne_etudiant

note1 = float(input("Entrez la première note1 : "))
note2 = float(input("Entrez la deuxième note2 : "))
note3 = float(input("Entrez la troisième note3 : "))

moyenne_etudiant = moyenne(note1, note2, note3)

if 15 <= moyenne_etudiant <= 20:
    message = "Très bon élève"
elif 11 <= moyenne_etudiant <= 14:
    message = "Bon élève"
elif 8 <= moyenne_etudiant <= 10:
    message = "Élève moyen"
elif 0 <= moyenne_etudiant <= 7:
    message = "Élève devant faire des efforts"
else:
    message = "Élève doit revoir ses priorités"

print(moyenne_etudiant, message)