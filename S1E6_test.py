

# Test de S1E6.py

def calcul_prix(nb):
    if nb <= 10:
        prix = nb * 0.1
    elif nb <= 20:
        prix = (10 * 0.1) + (nb - 10) * 0.08
    elif nb <= 50:
        prix = (10 * 0.1) + (10 * 0.08) + (nb - 20) * 0.06
    else:
        prix = (10 * 0.1) + (10 * 0.08) + (30 * 0.06) + (nb - 50) * 0.03
    return round(prix, 2)

def test_calcul_prix():
    assert calcul_prix(7) == 0.7
    assert calcul_prix(12) == 1.16
    assert calcul_prix(30) == 2.4
    assert calcul_prix(70) == 4.2

# pour lancer le test --> pytest S1E6_test.py
