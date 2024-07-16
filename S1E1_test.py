
# Test de S1E1.py
import pytest
from io import StringIO
import sys
from unittest.mock import patch

def test_de_l_inversion_des_variables():
    user_input = ["3", "7"]  # saisie utilisateur

    with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        import S1E1

    output = mock_stdout.getvalue()
    assert "Apres inversion :" in output
    assert "v1 vaut : 7" in output
    assert "v2 vaut : 3" in output

# pour lancer le test --> pytest S1E1_test.py
