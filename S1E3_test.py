

# Test de S1E3.py
import pytest
from io import StringIO
import sys
from unittest.mock import patch

def test_conversion_note():
    user_input = ["12"]  # saisie utilisateur

    with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        import S1E3

    output = mock_stdout.getvalue()
    assert "La lettre est : B" in output

# pour lancer le test --> pytest S1E3_test.py
