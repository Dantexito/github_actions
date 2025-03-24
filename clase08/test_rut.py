
from rut import validate

def test_rut_bueno():
    assert validate("11111111-1") == True

def test_rut_malo():
    assert validate("11111111-2") == False