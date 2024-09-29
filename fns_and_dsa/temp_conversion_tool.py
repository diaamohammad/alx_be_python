# تعريف المتغيرات العامة لعوامل التحويل
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# الدالة لتحويل الفهرنهايت إلى السيلسيوس
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# الدالة لتحويل السيلسيوس إلى الفهرنهايت
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# الدالة الرئيسية
def main():
    try:
        # طلب درجة الحرارة من المستخدم
        temperature_input = input("Enter the temperature to convert: ")
        
        # التحقق من صحة الإدخال (يجب أن يكون رقمي)
        if not temperature_input.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temperature_input)
        
        # طلب نوع درجة الحرارة (C أو F)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # التحقق من المدخلات وتنفيذ التحويل
        if unit == 'C':
            # تحويل من السيلسيوس إلى الفهرنهايت
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            # تحويل من الفهرنهايت إلى السيلسيوس
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as ve:
        # عرض رسالة خطأ في حالة إدخال قيمة غير صالحة
        print(f"Error: {ve}")
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
