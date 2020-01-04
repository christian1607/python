print("Hello world!!!  from christian")
print("World " * 10)
print(10 * "World ")

price = 10
rating = 5.9
name = "Christian"
isPython = False
print(price)

# Recibiendo inputs
#name = input("Ingrese su nombre: ")
#color = input("Ingrese tu color favorito: ")
#print(name + " likes " + color)


#convertir string a int
#birthDate = input('Ingrese anio de nacimiento: ')
#edad=2019-int(birthDate)
#print( edad)


# string grandes

# carta= '''
#     Hola Christian;
#     Esta es una carta hecha en python puedes ver el uso de 3 '
#
# '''
#
# print(carta)

#Buscando caracteres en string
#course = 'Python for everybody'
#print(course[-9]) # enpieza desde el otro lado
#print(course[0:2]) # substring de la cadena
#print(course[0:]) #Lista toda la cadena
#print(course[0:-10])


#formatted string
firstName = 'Christian'
lastName = 'Altamirano Ayala'

msg= f'{firstName} [{lastName}] is a coder'
print(msg)

#Strings methods
course="Python for Beginners"
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('e'))
print(course.replace("Beginners","Experts"))
print(course.__contains__("Python"))
print("Python" in course)

