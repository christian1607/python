customer = {
    "name": "Christian Altamirano Ayala",
    "Years": 26,
    "Single": True
}

print(customer.get("name"))
print(customer["name"])

phoneNumber= input("Ingress phone number: ")

number = {

    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero"
}
stringNumber=""
for digito in phoneNumber:
    stringNumber += number.get(digito)+" "

print(stringNumber)

