"""
I tried keeping the code readable, I used subTest and verbosity for specific failure
information, though these only work in terminal, it won't work if you use VSCode's
"run" button. I used "exit=False" so that the user won't get kicked out, without it,
that kept happening (I kept getting system exits). "verbosity=2" is there for additional
details.
"""

import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit

class TestTemperatureConversions(unittest.TestCase):

    def test_convert_celsius_to_kelvin(self):
        test_cases = [-100, -50, 0, 50, 100]
        expected = [173.15, 223.15, 273.15, 323.15, 373.15]
        for n, celsius in enumerate(test_cases):
            with self.subTest(celsius=celsius):
                result = convertCelsiusToKelvin(celsius)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_celsius_to_fahrenheit(self):
        test_cases = [-100, -50, 0, 50, 100]
        expected = [-148.0, -58.0, 32.0, 122.0, 212.0]
        for n, celsius in enumerate(test_cases):
            with self.subTest(celsius=celsius):
                result = convertCelsiusToFahrenheit(celsius)
                self.assertAlmostEqual(result, expected[n], places=2)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)