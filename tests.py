import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit

class TestTemperatureConversions(unittest.TestCase):

    def test_convert_celsius_to_kelvin(self):
        test_cases = [-100, -50, 0, 50, 100]
        expected = [173.15, 223.15, 273.15, 323.15, 373.15]
        for n, celsius in enumerate(test_cases):
            result = convertCelsiusToKelvin(celsius)
            print(f"Kelvin test {n+1}: convertCelsiusToKelvin({celsius}) returned {result}, expected {expected[n]}.")
            self.assertAlmostEqual(result, expected[n])

    def test_convert_celsius_to_fahrenheit(self):
        test_cases = [-100, -50, 0, 50, 100]
        expected = [-148, -58, 32, 122, 212]
        for n, celsius in enumerate(test_cases):
            result = convertCelsiusToFahrenheit(celsius)
            print(f"Fahrenheit test {n+1}: convertCelsiusToFahrenheit({celsius}) returned {result}, expected {expected[n]}.")
            self.assertAlmostEqual(result, expected[n], places=2)

if __name__ == "__main__":
    unittest.main(exit=False)