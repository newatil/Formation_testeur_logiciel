
"""
print("methode1")
# Demander à l'utilisateur de saisir le poids réel d'une pièce
poids_reel = float(input("Saisir le poids réel d'une pièce: "))

sac1 = 1
sac2 = 2
sac3 = 3

# Calculer le poids attendu si toutes les pièces étaient vraies
poids_attendu = (sac1 + sac2 + sac3) * poids_reel

# Calculer le poids trouvé en supposant que le premier sac contient les fausses pièces
poids_trouve = (sac1 * (poids_reel - 0.5)) + (sac2 * poids_reel) + (sac3 * poids_reel)

# Calculer la différence de poids
diff_poids = poids_attendu - poids_trouve

# Déterminer quel sac contient les fausses pièces en fonction de la différence de poids
if diff_poids == 0.5:
    print("Le sac 1 contient les fausses pièces")
elif diff_poids == 1.0:
    print("Le sac 2 contient les fausses pièces")
elif diff_poids == 1.5:
    print("Le sac 3 contient les fausses pièces")
else:
    print("Aucun sac ne contient de fausses pièces ou il y a une erreur dans les données")
    
"""

###################################################################################################### 

# Saisir le poids réel d'une pièce
poids_reel = float(input("Saisir le poids réel d'une pièce: "))

# On définit les poids des sacs contenant les pièces
sac1 = 1
sac2 = 2
sac3 = 3

# Calcul des poids des plateaux
# Plateau droit contient les 3 pièces du sac 3
plateau_droit = sac3 * poids_reel

# Plateau gauche contient 1 pièce du sac 1 + 2 pièces du sac 2
plateau_gauche = (sac1 * poids_reel) + (sac2 * poids_reel)

# Déterminer quel sac contient les fausses pièces en fonction du déséquilibre
if plateau_gauche < plateau_droit:
    diff = plateau_droit - plateau_gauche
    if diff == 0.5:
        print("Le sac 1 contient les fausses pièces")
    elif diff == 1:
        print("Le sac 2 contient les fausses pièces")
    else:
        print("Le sac 3 contient les fausses pièces")
else:
    print("Les poids sont équilibrés")



