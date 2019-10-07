names = ['Anddy', 'Christian', 'Lucero', 'Yamile', 'Evelyn']
print(names)

print(names[0])
print(names[0:2])

#

numbers = [6, 2, 3, 45, 23, 3, 4, 55, 3, 2, 4456, 7, 98, 6, 64, 4, 321, 4, 323, 6, 68, 2, 2, 12, 4, 5]

largeNumber = numbers[0]
for number in numbers:
    if number > largeNumber:
        largeNumber = number

print('The largest number is: ' + str(largeNumber))

numbers.append(1000)
print(numbers)

number2 = [0, 0, 0, 0, ]
number3 = numbers.__add__(number2)  # this method is immutable
print(number3)


numbersNoRepeted=[]
for item in numbers:
    if not numbersNoRepeted.__contains__(item):
        numbersNoRepeted.append(item)


print(numbersNoRepeted)