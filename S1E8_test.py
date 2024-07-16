

def calcul_delai(qte, mode):
    if mode == "rapide":
        if qte < 50:
            delai = 2
        elif qte < 100:
            delai = 3
        else:
            delai = 5
    else:
        if qte < 50:
            delai = 4
        elif qte < 100:
            delai = 5
        else:
            delai = 7
    return delai

def test_calcul_delai():
    assert calcul_delai(30, "rapide") == 2
    assert calcul_delai(300, "rapide") == 5 
    assert calcul_delai(30, "normal") == 4   
    assert calcul_delai(300, "normal") == 7  

# Exécute les tests si ce fichier est exécuté en tant que script principal
#if __name__ == "__main__":
    #pytest.main()

