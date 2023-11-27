def chiffrement_cesar(message, decalage):
    message_chiffre = ""

    for caractere in message:
        if caractere.isalpha():
            minuscule = caractere.islower()
            caractere = caractere.lower()

            # Effectue le décalage dans l'alphabet avec gestion du dépassement
            code_ascii = ord(caractere) - ord('a')
            nouveau_code_ascii = (code_ascii + decalage) % 26
            nouveau_caractere = chr(ord('a') + nouveau_code_ascii)

            # Reconvertit en majuscule si le caractère original était en majuscule
            if not minuscule:
                nouveau_caractere = nouveau_caractere.upper()

            message_chiffre += nouveau_caractere
        else:
            message_chiffre += caractere

    return message_chiffre

# Exemple d'utilisation
message_original = "Bonjour, comment ca va ?"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)

print(f"Message original : {message_original}")
print(f"Message chiffré : {message_chiffre}")