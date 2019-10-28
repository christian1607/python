# # if conditional
# hasGoodCredit = True
# price = 1000000
# if hasGoodCredit:
#     print(price * 0.1)
# else:
#     print(price * 0.2)
#
# hasHighIncome = False
# hasGoodCredit = True
#
# if hasGoodCredit and hasHighIncome:
#     print("Elegible for loan")
# else:
#     print("Not Elegible for loan")
#
#
# isMayorEdad = False
#
# #While conditional
# while not isMayorEdad:
#     edad = input("Ingrese su edad")
#     isMayorEdad = int(edad) >= 18
# print("Puede entrar a la discoteca")


for item in 'Christian':
    print(item)

print("=========")
for var in ['a','b','c','d']:
    print(var)



numbers = [5,2,5,2,2]
for x in numbers:
    print('X'*x)


# Define speak below:
def speak(animal='woof'):
    if animal == 'pig':
        return 'oink'
    elif animal == 'duck':
        return 'quack'
    elif animal == 'cat':
        return 'miau'
    elif animal == 'dog':
        return 'woof'
    elif animal == 'woof':
        return 'woof'
    else:
        return '?'