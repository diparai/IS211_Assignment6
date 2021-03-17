
def convertCelsiusToKelvin(number):

    given_number = float(number)
    default_kelvin = float(273.15)
    c_value = round(given_number + default_kelvin, 5)
    # print c_value
    return c_value
    



def convertCelsiusToFahrenheit(number):
    "Takes in a  float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"
    given_number = float(number)
    default_fahrenheit = float(32)
    c_value = round((given_number * 9 /5) + default_fahrenheit, 5)
    # print c_value
    return c_value

def convertKelvinToCelsius(number):

    given_number = float(number)
    default_celsius = float (273.15)
    c_value = round(given_number - default_celsius, 5)

    return c_value


def convertKelvinToFahrenheit(number):
    """
    Converts
    Celsius
    to
    Fahrenheit
    """
    given_number = float(number)
    defualt_fahrenheit = float(459.67)
    c_value = round((given_number * 9 / 5) - defualt_fahrenheit, 5)
    # print c_value
    return c_value


def convertFahrenheitToKelvin(number):

    given_number = float(number)
    default_kelvin = float(459.67)
    c_value = round((given_number + default_kelvin) * 5 / 9, 5)
# print c_value
    return c_value

def convertFahrenheitToCelsius(number):
    given_number = float(number)
    default_Celsius = float(32)
    c_value = round((given_number - default_Celsius) * 5 / 9, 5)
# print c_value
    return c_value

print (convertCelsiusToKelvin(300.111))
print(convertCelsiusToFahrenheit(300.45778))
print(convertFahrenheitToCelsius(36.9))
print(convertFahrenheitToKelvin(200.1))
print(convertKelvinToFahrenheit(25.36))
print(convertKelvinToCelsius(500))


