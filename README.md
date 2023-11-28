Chiffrement César

Ce script Python effectue un chiffrement César sur un message en utilisant un décalage spécifié par l’utilisateur.

Comment ça marche

L’algorithme décale chaque lettre du message d’entrée par un certain nombre de positions dans l’alphabet selon la méthode du chiffrement César.

	1.	Prérequis
	•	Python 3 installé
	2.	Utilisation
	•	Exécutez le script chiffrement_cesar.py.
	•	Entrez le message à chiffrer lorsque le programme le demande.
	•	Entrez le décalage souhaité.
	3.	Exemple
	•	Exemple d’utilisation :

Entrez le message à chiffrer : HELLO
Entrez le décalage souhaité : 3
Message original : HELLO
Message chiffré : KHOOR



Fonctionnalités

	•	Chiffrement de messages en utilisant la méthode du chiffrement César.
	•	Gestion des majuscules et des caractères non alphabétiques.


Chiffrement poly-alphabétique de Vigenère

Ce script Python permet de chiffrer un message en utilisant la méthode de substitution poly-alphabétique de Vigenère.

Comment ça marche

L’algorithme utilise une clé pour décaler les lettres du texte d’entrée selon un schéma poly-alphabétique. Voici comment l’exécuter :

	1.	Prérequis
	•	Python 3 installé
	2.	Utilisation
	•	Exécutez le script substitution_poly_alphabetiquetexte.py.
	•	Entrez le message à chiffrer lorsque le programme le demande.
	•	Entrez la clé de chiffrement.
	3.	Exemple
	•	Exemple d’utilisation :

Entrez le message à chiffrer : BONJOUR
Entrez la clé : CLE
Texte chiffré : DRPKQPT



Fonctionnalités

	•	Chiffrement de messages en utilisant la méthode de Vigenère.


Chiffrement Affine

Ce script Python permet de chiffrer un message en utilisant la méthode de chiffrement affine.

Comment ça marche

L’algorithme chiffre chaque lettre du texte d’entrée selon la formule mathématique : \(E(x) = (ax + b) \mod 26\), où  est l’index de la lettre dans l’alphabet,  et  sont des paramètres spécifiés par l’utilisateur.

	1.	Prérequis
	•	Python 3 installé
	2.	Utilisation
	•	Exécutez le script chiffrement_affine.py.
	•	Entrez le message à chiffrer lorsque le programme le demande.
	•	Entrez les valeurs de  et .
	3.	Exemple
	•	Exemple d’utilisation :

Entrez le message à chiffrer : HELLO
Entrez la valeur de 'a' : 5
Entrez la valeur de 'b' : 8
Texte chiffré : CMXXA



Fonctionnalités

	•	Chiffrement de messages en utilisant la méthode de chiffrement affine.
	•	Gestion des majuscules et des caractères non alphabétiques.

Remarques

	•	Ce script fonctionne avec des lettres majuscules seulement.
	•	Les valeurs de  et  doivent être des entiers.
