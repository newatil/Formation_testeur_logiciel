

# Test de S1E4.py
import pytest
from io import StringIO
import sys
from unittest.mock import patch

def test_calcul_ht_remises():
    user_input = ["3", "100"]  # Saisie utilisateur
    with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        import S1E4

    output = mock_stdout.getvalue()
    assert "Le montant HT apres remise vaut :  285" in output
    assert "Le montant de TVA vaut :  57" in output
    assert "Le montant TTC vaut :  342" in output

# pour lancer le test --> pytest S1E4_test.py
