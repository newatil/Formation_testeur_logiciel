

# Test de S1E2.py
import io
import sys
import pytest
from unittest.mock import patch

def test_calcul_tva_ttc(monkeypatch, capsys):
    inputs = ["100", "20"]  # Entrées simulées pour les saisies utilisateur
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    # Exécuter le code à tester
    exec(open("S1E2.py").read())

    captured = capsys.readouterr()
    assert captured.out == "Calcul TVA et TTC\nht vaut : 100.0\ntaux vaut : 20.0\nLe montant de la TVA vaut :  20.0\nLe montant TTC vaut :  120.0\n"

# pour lancer le test --> pytest S1E2_test.py
