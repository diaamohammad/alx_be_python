# تعريف عوامل التحويل العالمية
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """تحويل درجة الحرارة من فهرنهايت إلى مئوي"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """تحويل درجة الحرارة من مئوي إلى فهرنهايت"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # طلب إدخال درجة الحرارة من المستخدم
        temperature = float(input("أدخل درجة الحرارة للتحويل: "))
        unit = input("هل هذه الدرجة في مئوي (C) أم فهرنهايت (F)؟ (C/F): ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C هي {converted}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F هي {converted}°C")
        else:
            print("وحدة غير صالحة. يرجى إدخال 'C' أو 'F' فقط.")

    except ValueError:
        print("درجة حرارة غير صالحة. يرجى إدخال قيمة عددية.")

if __name__ == "__main__":
    main()
