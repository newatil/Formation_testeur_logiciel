
    
import pytest
from io import StringIO
import sys
from unittest.mock import patch

def test_de_l_inversion_des_variables():
    user_input = ["3", "7", "5"]  # saisie utilisateur

    with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        import sumoy

    output = mock_stdout.getvalue()
    assert "la somme des trois entiers est  15" in output
    assert "la moyenne des trois entiers est  5.0" in output
    assert "Le nombre entier le plus petit est : 3" in output
    assert "Le nombre entier le plus grand est : 7" in output

