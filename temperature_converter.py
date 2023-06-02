def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def celcius_to_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin * 9/5) - 459.67
    return fahrenheit

def main():
    print("Temperature Conversion")    
    print("======================")    
    print("1. Celcius to Fahrenheit")    
    print("2. Celcius to Kelvin")    
    print("3. Fahrenheit to Celcius")    
    print("4. Fahrenheit to Kelvin")    
    print("5. Kelvin to Celcius")    
    print("6. Kelvin to Fahrenheit")

    choice = int(input("Enter your choice between (1, 2, 3, 4, 5 or 6 ):"))
    
    if choice == 1:
        celcius = float(input("Enter temperature in Celcius: "))
        fahrenheit = celcius_to_fahrenheit(celcius)
        print(f"{celcius}°C = {fahrenheit}°F")
    elif choice == 2:
        celcius = float(input("Enter temperature in Celcius: "))
        kelvin = celcius_to_kelvin(celcius)
        print(f"{celcius}°C = {kelvin}K")
    elif choice == 3:
        fahrenheit = float(input("Enter temperature in fahrenheit: "))
        celcius = fahrenheit_to_celcius(fahrenheit)
        print(f"{fahrenheit}°F = {celcius}°C")
    elif choice == 4:
        fahrenheit = float(input("Enter temperature in fahrenheit: "))
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit}°F = {kelvin}K")
    elif choice == 5:
        kelvin = float(input("Enter temperature in kelvin: "))
        celcius = kelvin_to_celcius(kelvin)
        print(f"{kelvin}K = {celcius}°C")
    elif choice == 6:
        kelvin = float(input("Enter temperature in kelvin: "))
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin}K = {fahrenheit}°F")
    else:
        print("Invalid choice. Please choose between (1, 2, 3, 4, 5 or 6 )")    

if __name__ == '__main__':
    main()