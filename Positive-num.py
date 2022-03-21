list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input('enter the number:'))
    list.append(ele)
print(list)
print('The positive numbers in the list:')
for x in list:
    if(x>0):
        print(x)
