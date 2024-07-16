

print ("Calcul du prix des photocopies")
nb = int(input("Saisir votre nombre de photocopies : "))
print ("Le nombre de photocopies vaut : ", nb)
if nb <=  10:
	prix = nb * 0.1
elif nb <= 20:
	prix = (10 * 0.1) + (nb - 10) * 0.08
elif nb <= 50:
	prix = (10 * 0.1) + (10 * 0.08) + (nb - 20) * 0.06
else: prix = (10 * 0.1) + (10 * 0.08) + (30 * 0.06) + (nb - 50) * 0.03
print ("Le prix est : ", round(prix,2))
