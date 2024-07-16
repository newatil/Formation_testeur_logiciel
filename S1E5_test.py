

# Test de S1E5.py

def choix_offre(conso):
    if (10 + conso*0.5) < (20 + conso * 0.2):
        print ("Il faut choisir l'offre 1")
        offre = 1
    elif (10 + conso*0.5) > (20 + conso * 0.2):
        print ("Il faut choisir l'offre 2")
        offre = 2
    else: 
        print ("Les deux offres sont équivalentes")
        offre = 3
    return(offre)

def test_choix_offre():
    assert choix_offre(10) == 1
    assert choix_offre(30) == 1
    assert choix_offre(35) == 2
    assert choix_offre(80) == 2

# pour lancer le test --> pytest S1E5_test.py

