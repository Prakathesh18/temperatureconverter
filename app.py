def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("=== Temperature Converter Menu ===")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius (Coming Soon in Push 2)")
    
    choice = input("Select an option (1-2): ")
    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C is equal to {celsius_to_fahrenheit(c):.2f}°F")
    else:
        print("Option not available yet.")

if __name__ == "__main__":
    main()
