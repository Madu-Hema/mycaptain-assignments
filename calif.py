print("Enter two numbers: ")
num1 = int(input())
num2 = int(input())
choice = int(input("Enter your choice:"))
if choice == 1:
    print('addition of numbers')
    res = num1 + num2
    print(res)
elif choice == 2:
    print('subtraction of numbers')
    res = num1 - num2
    print(res)
elif choice == 3:
    print('multiplicatoin of numberd')
    res = num1 * num2
    print(res)
elif choice == 4:
    print('division of numbers')
    res = num1 / num2
    print(res)
else:
  print("Wrong input..!!")
