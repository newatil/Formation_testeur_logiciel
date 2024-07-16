
print ("Calcul TVA et TTC")
ht = float(input("Saisir un montant HT : "))
print ("ht vaut :", ht)
taux = float(input("Saisir un taux de TVA : "))
print ("taux vaut :", taux)
tva = ht * (taux / 100)
print ("Le montant de la TVA vaut : ", round(tva,2)) 
ttc = ht + tva
print ("Le montant TTC vaut : ", round(ttc,2))

