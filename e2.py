number = input(" What is the number: ")
number = int(number)

a = number % 2
a = int(a)

b = number % 4
b = int(b)

if a == 0 and a != b:
    print(" Number is even")
elif b == 0:
    print(" number is multiple of 4")
else:
    print(" Number is odd")

num = input(" What is the first number: ")
num = int(num)
check = input(" What is the other check number: ")
check = int(check)

if num % check == 0:
    print(" it can be divided ")
else:
    print(" it Cannot be divided")
