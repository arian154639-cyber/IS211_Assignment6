"""
This wasn't the most efficient way to do this, but I wanted to keep the structure the same
as the other test scripts. This still uses "exit=False" and "verbosity=2".
"""

import unittest
from conversions3 import TemperatureAndDistanceConverter, ConversionNotPossible

class TestTemperatureAndDistanceConversion(unittest.TestCase):

    def test_convert_celsius_to_kelvin(self):
        test_cases = [0, 1]
        expected = [273.15, 274.15]
        for n, value in enumerate(test_cases):
            with self.subTest(celsius=value):
                result = TemperatureAndDistanceConverter("Celsius", "Kelvin", value)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_celsius_to_fahrenheit(self):
        test_cases = [0, 1]
        expected = [32, 33.8]
        for n, value in enumerate(test_cases):
            with self.subTest(celsius=value):
                result = TemperatureAndDistanceConverter("Celsius", "Fahrenheit", value)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_fahrenheit_to_celsius(self):
        test_cases = [0, 1]
        expected = [-17.78, -17.22]
        for n, value in enumerate(test_cases):
            with self.subTest(fahrenheit=value):
                result = TemperatureAndDistanceConverter("Fahrenheit", "Celsius", value)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_fahrenheit_to_kelvin(self):
        test_cases = [0, 1]
        expected = [255.37, 255.93]
        for n, value in enumerate(test_cases):
            with self.subTest(fahrenheit=value):
                result = TemperatureAndDistanceConverter("Fahrenheit", "Kelvin", value)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_kelvin_to_fahrenheit(self):
        test_cases = [0, 1]
        expected = [-459.67, -457.87]
        for n, value in enumerate(test_cases):
            with self.subTest(kelvin=value):
                result = TemperatureAndDistanceConverter("Kelvin", "Fahrenheit", value)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_kelvin_to_celsius(self):
        test_cases = [0, 1]
        expected = [-273.15, -272.15]
        for n, value in enumerate(test_cases):
            with self.subTest(kelvin=value):
                result = TemperatureAndDistanceConverter("Kelvin", "Celsius", value)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_meters_to_yards(self):
        test_cases = [0, 1]
        expected = [0, 1/0.9144]
        for n, value in enumerate(test_cases):
            with self.subTest(meters=value):
                result = TemperatureAndDistanceConverter("Meters", "Yards", value)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_meters_to_miles(self):
        test_cases = [0, 1]
        expected = [0, 1/1609.34]
        for n, value in enumerate(test_cases):
            with self.subTest(meters=value):
                result = TemperatureAndDistanceConverter("Meters", "Miles", value)
                self.assertAlmostEqual(result, expected[n], places=2)
    
    def test_convert_yards_to_meters(self):
        test_cases = [0, 1]
        expected = [0, 1 * 0.9144]
        for n, value in enumerate(test_cases):
            with self.subTest(yards=value):
                result = TemperatureAndDistanceConverter("Yards", "Meters", value)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_yards_to_miles(self):
        test_cases = [0, 1]
        expected = [0, 1 / 1760]
        for n, value in enumerate(test_cases):
            with self.subTest(yards=value):
                result = TemperatureAndDistanceConverter("Yards", "Miles", value)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_miles_to_meters(self):
        test_cases = [0, 1]
        expected = [0, 1 * 1609.34]
        for n, value in enumerate(test_cases):
            with self.subTest(miles=value):
                result = TemperatureAndDistanceConverter("Miles", "Meters", value)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_convert_miles_to_yards(self):
        test_cases = [0, 1]
        expected = [0, 1760]
        for n, value in enumerate(test_cases):
            with self.subTest(miles=value):
                result = TemperatureAndDistanceConverter("Miles", "Yards", value)
                self.assertAlmostEqual(result, expected[n], places=2)

    def test_identity_conversions(self):
        units = ["Celsius", "Fahrenheit", "Kelvin", "Meters", "Yards", "Miles"]
        for unit in units:
            for value in [0.5, 100.5]:
                with self.subTest(unit=unit, value=value):
                    result = TemperatureAndDistanceConverter(unit, unit, value)
                    self.assertAlmostEqual(result, value, places=2)

    def test_invalid_conversion(self):
        with self.assertRaises(ConversionNotPossible):
            TemperatureAndDistanceConverter("Celsius", "Miles", 100)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)