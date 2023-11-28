def chiffrement_affine(texte, a, b):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texte_chiffre = ''
    
    for lettre in texte:
        if lettre in alphabet:
            index_lettre = alphabet.index(lettre)
            index_chiffre = (a * index_lettre + b) % 26
            lettre_chiffree = alphabet[index_chiffre]
            texte_chiffre += lettre_chiffree
        else:
            texte_chiffre += lettre
    
    return texte_chiffre

texte_a_chiffrer = input("Entrez le message à chiffrer : ")
a = int(input("Entrez la valeur de 'a' : "))
b = int(input("Entrez la valeur de 'b' : "))
texte_chiffre = chiffrement_affine(texte_a_chiffrer, a, b)
print("Texte chiffré :",texte_chiffre)