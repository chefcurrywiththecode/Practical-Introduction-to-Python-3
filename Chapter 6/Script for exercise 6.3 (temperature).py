""" convert_cel_to_far() which takes one float parameter representing
degrees Celsius and returns a float representing the same temperature
in degrees Fahrenheit using the following formula: """

def convert_cel_to_far(celsius):
    farenheit = celsius * 9/5 + 32
    return farenheit

print((f'{convert_cel_to_far(30):.2f}'))


""" convert_far_to_cel() which take one float parameter representing
degrees Fahrenheit and returns a float representing the same temperature
in degrees Celsius using the following formula: """

def convert_far_to_cel(farenheit):
    celsius = (farenheit- 32) * 5/9
    return celsius

print((f'{convert_far_to_cel(100):.2f}'))