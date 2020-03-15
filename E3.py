a = [1, 90, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in a:
      if(element < 5):
          print(element)
          b = [element]

number = input(" What is the number: ")
number = int(number)
for element in a:
    if (element < number):
        print(element)


