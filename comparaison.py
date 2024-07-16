
# tableau d'entiers
tab = [15, 22, 8, 19, 31, 42, 3, 27, 10, 5]

# Initialiser val_min et val_max avec le premier élément du tableau
val_min = tab[0]
val_max = tab[0]

# Parcourir chaque élément du tableau
for element in tab:
    # Vérifier si l'élément est plus petit que val_min
    if element < val_min:
        val_min = element
    # Vérifier si l'élément est plus grand que val_max
    if element > val_max:
        val_max = element

# Afficher les résultats
print("La plus petite valeur est :", val_min)
print("La plus grande valeur est :", val_max)
