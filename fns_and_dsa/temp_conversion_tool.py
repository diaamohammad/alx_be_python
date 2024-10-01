FAHRENHEIT_TO_CELSIUS_FACTOR=(5 / 9 ) # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR=(9 / 5 )  # Conversion factor from Celsius to Fahrenheit

def convert_to_celsius(fahrenheit):

    
    return(fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32


def main():

    tempersture =float(input("enter the number of temberature"))

    unit = input("Is this temperature in Celsius (C) or Fahrenheit (F)? (C/F): ").strip().upper()

    if unit =="C":

        convert = convert_to_fahrenheit(tempersture)

        print(f"{tempersture} in f is {convert}")
    
    elif unit =="F":
        convert=convert_to_celsius(tempersture)
        print(f"{tempersture} in c is {convert}")

    else:
        print("invaild option")

if __name__ == "__main__":
    main()