# طلب الإدخال من المستخدم
size = int(input("Enter the size of the pattern: "))

# التأكد من أن الحجم المدخل موجب
while size <= 0:
    size = int(input("Please enter a positive integer: "))

# بدء رسم المربع
row = 0

# استخدام حلقة while لتكرار الصفوف
while row < size:
    # حلقة for لتكرار الأعمدة وطباعتها في نفس الصف
    for col in range(size):
        print("*", end="")
    print()  # الانتقال إلى سطر جديد بعد الانتهاء من الصف
    row += 1  # زيادة عدد الصفوف
