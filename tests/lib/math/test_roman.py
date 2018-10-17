
from pitoolbox.lib.math.roman import decimal_to_roman


def test_roman():
	assert decimal_to_roman(1000) == 'M'
	assert decimal_to_roman(1989) == 'MCMLXXXIX'
