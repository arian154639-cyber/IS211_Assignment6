"""
I tried keeping the code readable, I used subTest and verbosity for specific failure
information, though these only work in terminal, it won't work if you use VSCode's
"run" button. I used "exit=False" so that the user won't get kicked out. This is 
basically the same script as tests.py but now it uses conversions2.py so the conversions
actually work, and there's six tests now instead of just two.
"""

import unittest
from conversions2 import convertCelsiusToKelvin, convertCelsiusToFahrenheit, convertFahrenheitToCelsius, convertFahrenheitToKelvin, convertKelvinToCelsius, convertKelvinToFahrenheit

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

    def test_convert_fahrenheit_to_celsius(self):
        test_cases = [-100, -50, 0, 50, 100]
        expected = [-73.33, -45.56, -17.77, 10.0, 37.78]
        for n, fahrenheit in enumerate(test_cases):
            with self.subTest(fahrenheit=fahrenheit):
                result = convertFahrenheitToCelsius(fahrenheit)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_fahrenheit_to_kelvin(self):
        test_cases = [-100, -50, 0, 50, 100]
        expected = [199.82, 227.59, 255.37, 283.15, 310.93]
        for n, fahrenheit in enumerate(test_cases):
            with self.subTest(fahrenheit=fahrenheit):
                result = convertFahrenheitToKelvin(fahrenheit)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_kelvins_to_fahrenheit(self):
        test_cases = [0, 50, 100, 150, 200]
        expected = [-459.67, -369.67, -279.67, -189.67, -99.67]
        for n, kelvins in enumerate(test_cases):
            with self.subTest(kelvins=kelvins):
                result = convertKelvinToFahrenheit(kelvins)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_kelvins_to_celsius(self):
        test_cases = [0, 50, 100, 150, 200]
        expected = [-273.15, -223.15, -173.15, -123.15, -73.15]
        for n, kelvins in enumerate(test_cases):
            with self.subTest(kelvins=kelvins):
                result = convertKelvinToCelsius(kelvins)
                self.assertAlmostEqual(result, expected[n], places=2)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)