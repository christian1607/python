customer = {
    "name": "Christian Altamirano Ayala",
    "Years": 26,
    "Single": True
}

print(customer.get("name"))
print(customer["name"])

for value in customer.values():
    print(value)


for key in customer.keys():
    print(key)

for k,v in customer.items():
    print(f"Key: {k} Value: {v}")

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




dicti = {}
def multiple_letter_count(string):
    for lt in string:
        print(lt)
        print(dicti.get(lt))
        if dicti.get(lt) is None:
            dicti[lt] = 1
        else:
            dicti[lt] = dicti[lt]+1

    return dicti


print(multiple_letter_count("awesome"))