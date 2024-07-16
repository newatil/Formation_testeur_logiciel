
 #tableau d'entiers
tab = [4, 2, 9, 7, 2, 4, 6, 4, 2, 1]

# Faire saisir un entier à l'utilisateur
nb_recherche = int(input("Entrez un entier : "))

# Initialiser le compteur à 0
cp = 0

# Parcourir chaque élément du tableau
for e in tab:
    # Vérifier si l'élément est égal à l'entier recherché
    if e == nb_recherche:
        cp += 1

# Afficher le résultat
if cp > 0:
    print(f"Le chifre {nb_recherche} est présent {cp} fois dans le tableau.")
else:
    print(f"Le chifre {nb_recherche} n'est pas présent dans le tableau.")
