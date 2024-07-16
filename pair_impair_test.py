

import pytest
from io import StringIO
import sys
from unittest.mock import patch

def test_pair_impair():
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        import pair_impair

    output = mock_stdout.getvalue()
    assert "11 est impair" in output
    assert "20 est pair" in output
    assert "36 est pair" in output
    assert "45 est impair" in output
    assert "58 est pair" in output
    assert "67 est impair" in output
    assert "74 est pair" in output
    assert "83 est impair" in output
    assert "92 est pair" in output
    assert "101 est impair" in output

