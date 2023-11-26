def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("\n\t\tTemperature Conversion Program")
    print("\t\t1. Celsius to Fahrenheit")
    print("\t\t2. Fahrenheit to Celsius")

    choice = int(input("\n\t\tEnter your choice (1 or 2): "))

    if choice == 1:
        celsius = float(input("\n\t\tEnter temperature in Celsius: "))
        converted_temperature = celsius_to_fahrenheit(celsius)
        print(f"\t\t{celsius} degrees Celsius is equal to {converted_temperature:.2f} degrees Fahrenheit.\n")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        converted_temperature = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is equal to {converted_temperature:.2f} degrees Celsius.")

    else:
        print("Invalid choice. Please enter either 1 or 2.")

if __name__ == "__main__":
    main()
