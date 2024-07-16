
import pytest
from io import StringIO
import sys
from unittest.mock import patch

def test_de_l_inversion_des_variables():
    user_input = ["30"]  # saisie utilisateur

    with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        import elections

    output = mock_stdout.getvalue()
    assert "Candidat qualifié pour le second tour" in output
    

