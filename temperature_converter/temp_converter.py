class TemperatureConverter:
    def __init__(self, name):
        self.name = name
        
    def fahrenheit_to_celsius(self, temp_f):
        if temp_f < -459.67:
            return "Temperature cannot be below absolute zero (-459.67°F)"
        else:
            temp_c = (temp_f - 32) * 5/9
            return temp_c
        
    def celsius_to_fahrenheit(self, temp_c):
        if temp_c < -273.15:
            return "Temperature cannot be below absolute zero (-273.15°C)"
        else:
            temp_f = (temp_c * 9/5) + 32
            return temp_f
        
    def kelvin_to_celsius(self, temp_k):
        if temp_k < 0:
            return "Temperature cannot be below absolute zero (0K)"
        else:
            temp_c = temp_k - 273.15
            return temp_c
        
    def celsius_to_kelvin(self, temp_c):
        if temp_c < -273.15:
            return "Temperature cannot be below absolute zero (-273.15°C)"
        else:
            temp_k = temp_c + 273.15
            return temp_k
        
    def fahrenheit_to_kelvin(self, temp_f):
        if temp_f < -459.67:
            return "Temperature cannot be below absolute zero (-459.67°F)"
        else:
            temp_k = (temp_f + 459.67) * 5/9
            return temp_k
        
    def kelvin_to_fahrenheit(self, temp_k):
        if temp_k < 0:
            return "Temperature cannot be below absolute zero (0K)"
        else:
            temp_f = (temp_k * 9/5) - 459.67
            return temp_f

print("Welcome to Temperature Converter!")
name = input("What's your name? ")
converter = TemperatureConverter(name)

while True:
    print("\nChoose a temperature scale to convert from:\n")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    print("4. Exit")
    choice1 = input("Enter your choice (1-4): ")
    
    if choice1 == '1':
        # Convert Celsius to Fahrenheit or Kelvin
        print("Enter the temperature in Celsius:")
        celsius = float(input())

        if celsius < -273.15:
            print("Invalid input. Celsius temperature cannot be below -273.15.")
            continue
        print("Select the temperature scale you want to convert to:")
        print("1. Fahrenheit")
        print("2. Kelvin")
        
        choice2 = input("Enter choice (1/2): ")

        if choice2 == '1':
            # Convert Celsius to Fahrenheit
            fahrenheit = round((celsius * 1.8) + 32, 2)
            print(f"{name}, {celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
        elif choice2 == '2':
            # Convert Celsius to Kelvin
            kelvin = round(celsius + 273.15, 2)
            print(f"{name}, {celsius} Celsius is equal to {kelvin} Kelvin.")
        else:
            print("Invalid input. Please select a valid option.")

    elif choice1 == '2':
        # Convert Fahrenheit to Celsius or Kelvin
        print("Enter the temperature in Fahrenheit:")
        fahrenheit = float(input())

        if fahrenheit < -459.67:
            print("Invalid input. Fahrenheit temperature cannot be below -459.67.")
            continue

        print("Select the temperature scale you want to convert to:")
        print("1. Celsius")
        print("2. Kelvin")
        choice2 = input("Enter choice (1/2): ")

        if choice2 == '1':
            # Convert Fahrenheit to Celsius
            celsius = round((fahrenheit - 32) / 1.8, 2)
            print(f"{name}, {fahrenheit} Fahrenheit is equal to {celsius} Celsius.")
        elif choice2 == '2':
            # Convert Fahrenheit to Kelvin
            kelvin = round((fahrenheit + 459.67) * 5/9, 2)
            print(f"{name}, {fahrenheit} Fahrenheit is equal to {kelvin} Kelvin.")
        else:
            print("Invalid input. Please select a valid option.")

    elif choice1 == '3':
        # Convert Kelvin to Celsius or Fahrenheit
        print("Enter the temperature in Kelvin:")
        kelvin = float(input())

        if kelvin < 0:
            print("Invalid input. Kelvin temperature cannot be below 0.")
            continue

        print("Select the temperature scale you want to convert to:")
        print("1. Celsius")
        print("2. Fahrenheit")
        choice2 = input("Enter choice (1/2): ")

        if choice2 == '1':
            # Convert Kelvin to Celsius
            celsius = round(kelvin - 273.15, 2)
            print(f"{name}, {kelvin} Kelvin is equal to {celsius} Celsius.")
        elif choice2 == '2':
            # Convert Kelvin to Fahrenheit
            fahrenheit = round((kelvin * 9/5) - 459.67, 2)
            print(f"{name}, {kelvin} Kelvin is equal to {fahrenheit} Fahrenheit.")
        else:
            print("Invalid input. Please select a valid option.")

    elif choice1 == '4':
        # Exit the program
        print(f"Thank you, {name}. See you next time!")
        break

    else:
        print("Invalid input. Please select a valid option.")
