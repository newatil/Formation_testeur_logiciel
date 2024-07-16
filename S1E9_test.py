
# Test de S1E1.py
import pytest
from io import StringIO
import sys
from unittest.mock import patch

def test_de_verification_des_dates():
    user_input = ["12","3","1991","7","2","1971"]  # saisie utilisateur

    with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        import S1E9

    output = mock_stdout.getvalue()
    assert "La date 2 est la plus ancienne" in output
    assert "La date 2 est la plus ancienne" in output
    assert "La date 2 est la plus ancienne" in output
  

