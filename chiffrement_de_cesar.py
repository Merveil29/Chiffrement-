def chiffrement_cesar(msg, decalage):
    resultat = ""
    for lettre in msg:
        if lettre.isalpha():
            majuscule = lettre.isupper()
            ascii_lettre = ord(lettre)
            ascii_lettre = (ascii_lettre - ord('A' if majuscule else 'a') + decalage) % 26 + ord('A' if majuscule else 'a')
            lettre_chiffree = chr(ascii_lettre)
            resultat += lettre_chiffree
        else:
            resultat += lettre
    return resultat

def saisie_utilisateur():
    message = input("Entrez le message à chiffrer : ")
    decalage = int(input("Entrez le décalage souhaité : "))
    return message, decalage

def afficher_resultats(msg_original, msg_chiffre):
    print("Message original : ", msg_original)
    print("Message chiffré : ", msg_chiffre)

message, decalage = saisie_utilisateur()
message_chiffre = chiffrement_cesar(message, decalage)
afficher_resultats(message, message_chiffre)