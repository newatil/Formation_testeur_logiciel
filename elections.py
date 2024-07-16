

print("Algorithme d'elections")

# Faire saisir le pourcentage des voix obtenues par le candidat
pourcentage = float(input("Entrez le pourcentage des voix obtenues par le candidat : "))
    
    # Affichage du statut en fonction du pourcentage
if pourcentage < 5:
	print("Candidat éliminé")
elif 5 <= pourcentage < 50:
	print("Candidat qualifié pour le second tour")
elif pourcentage >= 50:
	print("Candidat élu")
