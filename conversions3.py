"""
I tried to keep this concise, so instead of repeating formulas, I used base units
(celsius and meters) to keep the code short.
"""

class ConversionNotPossible(Exception):
    pass

def TemperatureAndDistanceConverter(fromUnit, toUnit, value):
    temperature_units = {"Celsius", "Fahrenheit", "Kelvin"}
    distance_units = {"Meters", "Yards", "Miles"}

    if fromUnit in temperature_units and toUnit in temperature_units:
        if fromUnit == "Celsius":
            celsius = value
        elif fromUnit == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif fromUnit == "Kelvin":
            celsius = value - 273.15

        if toUnit == "Celsius":
            return celsius
        elif toUnit == "Fahrenheit":
            return (celsius * 9/5) + 32
        elif toUnit == "Kelvin":
            return celsius + 273.15

    elif fromUnit in distance_units and toUnit in distance_units:
        meters = (
            value if fromUnit == "Meters" else
            value * 0.9144 if fromUnit == "Yards" else
            value * 1609.34
        )

        if toUnit == "Meters":
            return meters
        elif toUnit == "Yards":
            return meters / 0.9144
        elif toUnit == "Miles":
            return meters / 1609.34

    raise ConversionNotPossible("These units cannot be converted.")