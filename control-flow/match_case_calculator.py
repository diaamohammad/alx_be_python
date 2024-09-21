#promt the numbers from user

num1 = int(input("Enter the first number:"))

num2 = int (input("Enter the second number:"))

#ask for operation

his_choose = input("choose the operation (+,-,*,/):")

#check

match his_choose:
    case"+":
        print(f"result is {num1+num2}")

    case"-":
        print(f"result is {num1-num2}")

    case"*":
        print(f"result is {num1*num2}")

    case"/":
        print(f"result is {num1/num2}")

    case _:
        print("not option")