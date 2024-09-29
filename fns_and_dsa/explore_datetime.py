from datetime import datetime, timedelta

# الجزء الأول: عرض التاريخ والوقت الحاليين
def display_current_datetime():
    # الحصول على التاريخ والوقت الحاليين
    current_date = datetime.now()
    # طباعة التاريخ والوقت بصيغة "YYYY-MM-DD HH:MM:SS"
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# الجزء الثاني: حساب تاريخ مستقبلي
def calculate_future_date(days):
    # الحصول على التاريخ الحالي
    current_date = datetime.now()
    # إضافة عدد الأيام المحدد لحساب التاريخ المستقبلي
    future_date = current_date + timedelta(days=days)
    # طباعة التاريخ المستقبلي بصيغة "YYYY-MM-DD"
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # عرض التاريخ والوقت الحاليين
    display_current_datetime()

    # سؤال المستخدم عن عدد الأيام لإضافتها
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # حساب وعرض التاريخ المستقبلي
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
