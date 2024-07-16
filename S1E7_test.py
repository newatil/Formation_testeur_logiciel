
# Test de S1E7.py

def calcul_tarif(pu):
    if pu < 20:
        pu = pu * 1.1
    elif pu < 50:
        pu = pu * 1.075
    elif pu < 100:
        pu = pu * 1.05
    else:
        pu = pu * 1.025
    return round(pu, 2)

def test_calcul_tarif():
    assert calcul_tarif(10) == 11
    assert calcul_tarif(30) == 32.25
    assert calcul_tarif(70) == 73.5
    assert calcul_tarif(200) == 205

# pour lancer le test --> pytest S1E7_test.py

