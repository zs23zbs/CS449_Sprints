import pytest

def f(): 
    raise SystemExit(1)

def test_myselt():
    with pytest.raises(SystemExit):
        f()