#promt the numbers from user

num1 = int(input("Enter the first number:"))

num2 = int (input("Enter the second number:"))

#ask for operation

operation = input("choose the operation (+,-,*,/):")

#check

match operation:
    case"+":
        print(f"The result is {num1+num2}")

    case"-":
        print(f"The result is {num1-num2}")

    case"*":
        print(f"The result is {num1*num2}")

    case"/":
        print(f"The result is {num1/num2}")

    case _:
        print("not option")