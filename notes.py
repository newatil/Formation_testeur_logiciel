
#tableau des notes
tab_notes = [12.5, 9.8, 15.0, 10.0, 7.5, 18.0, 13.0, 5.0, 11.2, 6.3]

# Initialiser le compteur à 0
compteur = 0

# Parcourir chaque note dans le tableau
for note in tab_notes:
    # Vérifier si la note est supérieure ou égale à 10
    if note >= 10:
        compteur += 1

# Afficher le nombre d'étudiants ayant obtenu la moyenne
print("Nombre d'étudiants ayant obtenu la moyenne :", compteur)
