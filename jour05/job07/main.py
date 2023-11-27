def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            prochain_multiple_de_cinq = (note // 5 + 1) * 5
            if prochain_multiple_de_cinq - note < 3:
                notes_arrondies.append(prochain_multiple_de_cinq)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

L = [38, 42, 78, 89, 91, 94, 97]
L_arrondies = arrondir_notes(L)

print("Notes originales :", L)
print("Notes arrondies  :", L_arrondies)