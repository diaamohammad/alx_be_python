def display_menu():
    # يجب أن تكون طباعة الجملة كما هو مطلوب في الاختبار
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # قائمة التسوق
    
    while True:
        display_menu()  # استدعاء دالة عرض القائمة
        try:
            # يجب التأكد من أن الإدخال رقم
            choice = int(input("Enter your choice (1-4): "))  # إدخال المستخدم كرقم
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue  # إعادة الطلب من المستخدم إذا كان الإدخال غير صحيح
        
        if choice == 1:  # إضافة عنصر إلى القائمة
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        
        elif choice == 2:  # إزالة عنصر من القائمة
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == 3:  # عرض القائمة الحالية
            if shopping_list:
                print("\nShopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == 4:  # الخروج من البرنامج
            print("Goodbye!")
            break
        
        else:  # التعامل مع خيار غير صحيح
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

