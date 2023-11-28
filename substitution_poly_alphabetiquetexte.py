def substitution_poly_alphabetique(texte, cle):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texte = texte.upper()
    cle = cle.upper()
    cle_etendue = ''.join(cle[i % len(cle)] if lettre.isalpha() else lettre for i, lettre in enumerate(texte))
    
    texte_chiffre = ''
    for i, lettre in enumerate(texte):
        if lettre in alphabet:
            index_texte = alphabet.find(lettre)
            index_cle = alphabet.find(cle_etendue[i])
            index_chiffre = (index_texte + index_cle) % 26
            texte_chiffre += alphabet[index_chiffre]
        else:
            texte_chiffre += lettre
    
    return texte_chiffre

texte_a_chiffrer = input("Entrez le message à chiffrer : ")
cle = input("Entrez la clé : ")
texte_chiffre = substitution_poly_alphabetique(texte_a_chiffrer, cle)
print("Texte chiffré :",texte_chiffre)