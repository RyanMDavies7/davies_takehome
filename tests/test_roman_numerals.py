import pytest
from src.roman_numerals.convert import from_roman

def test_from_roman():
    assert from_roman("I") == 1
    assert from_roman("V") == 5
    assert from_roman("X") == 10
    assert from_roman("MCMXC") == 1990
    assert from_roman("MMVIII") == 2008
    assert from_roman('MCMLXIX') == 1969
