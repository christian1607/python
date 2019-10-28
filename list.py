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
    #if item in numbersNoRepeted
        numbersNoRepeted.append(item)


print(numbersNoRepeted)


datos = ["gato", 2]
print(datos)

# datos.append(3,2,2) doesn't work
datos.append([2,2,2,2,2]) # this add an array as element of the existing array,
print(datos)

datos.extend([2,3,4,5,6,]) # this join arrays
print(datos)
