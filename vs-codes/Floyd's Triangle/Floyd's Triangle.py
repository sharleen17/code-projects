#Floyd's Triangle

row = int(input("Enter your preferred number of rows: "))

number = 1

for i in range(row):
    for j in range(i + 1):
        print(number, end=" ")
        number += 1
    print() #To change the line.
