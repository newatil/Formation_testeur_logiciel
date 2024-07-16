
import pytest
from io import StringIO
import sys
from unittest.mock import patch

def test_nombre_etudiants_ayant_la_moyenne():
    
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        import notes

    output = mock_stdout.getvalue()
    assert "Nombre d'étudiants ayant obtenu la moyenne : 6" in output

