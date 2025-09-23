FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius (fahrenheit):
    temp = (fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR) + 32
    return temp

def convert_to_fahrenheit (celsius):
    temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temp

def main ():
    temprature = input("Enter the temperature to convert: ")
    temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

    if temp_type == "C":
        print(f"{temprature}°C is {convert_to_fahrenheit(temprature)}°F")
    elif temp_type == "F":
        print(f"{temprature}°F is {convert_to_celsius(temprature)}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")