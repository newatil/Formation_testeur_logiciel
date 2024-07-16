
import pytest
from io import StringIO
import sys
from unittest.mock import patch

def test_comparaison():

    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        import comparaison

    output = mock_stdout.getvalue()
    assert "La plus petite valeur est : 3" in output
    assert "La plus grande valeur est : 42" in output


