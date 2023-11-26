def chiffrement_cesar(texte, decalage):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texte_chiffre = ''

    for lettre in texte:
        if lettre in alphabet:
            index_lettre = alphabet.index(lettre)
            index_chiffre = (index_lettre + decalage) % 26
            lettre_chiffree = alphabet[index_chiffre]
            texte_chiffre += lettre_chiffree
        else:
            texte_chiffre += lettre

    return texte_chiffre

texte_a_chiffrer = "CECI EST UN MESSAGE SECRET"
decalage = 3
texte_chiffre = chiffrement_cesar(texte_a_chiffrer, decalage)
print("Texte chiffré :",texte_chiffre)