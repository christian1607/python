def divide(num1, num2):

    try:
        return num1/num2
    except TypeError:
        print ("Please provide two integers or floats")
    except ZeroDivisionError:
        print ("Please do not divide by zero")


divide(1, 0)

try:
    age = int(input("Ingrese un numero ()"))
    print(age)
except ValueError:
    print("Numero invalido")


def colorize(text, color):

    if type(text) is not str:
        raise ValueError("texto debe ser un valor literal")

    print(f"Printed: {text} in color: {color}")


colorize("Domain Drive Desing", "blue")


try:
    number=int(input("Ingrese un numero: "))
    print("You've ingress :" + str(number))
except Exception:
    print("It's not a number")
else:
    print("this run when no exception occurs")
finally:
    print("Finally run this code")