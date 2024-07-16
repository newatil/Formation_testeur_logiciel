
import pytest
from io import StringIO
import sys
from unittest.mock import patch

def test_nombre_de_presence():
    user_input = ["2"]  # saisie utilisateur

    with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        import presence

    output = mock_stdout.getvalue()
    assert "Le chifre 2 est présent 3 fois dans le tableau." in output
