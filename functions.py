def greet_user():
    print("Hi there")
    print("Welcome aboard")


def greet_user_name(name="world"):
    print("Hi " + name)
    print("Welcome aboard")


def square(number):
    return number * number


def full_name (first_name,last_name):
    """Return fullname string"""
    print(f'{first_name} {last_name}')


print("Start")
greet_user_name("Christian")
print("Finish")

full_name("christian",'altamirano')
full_name(last_name="Altamirano",first_name="Christain")
full_name.__doc__