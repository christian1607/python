class User:

    #Class variable
    cant_login = 0

    @classmethod
    def display_users_active(cls):
        print(cls.cant_login)

    def __init__(self, name, last_name=''):
        self.nombre = name
        self.apellido = last_name
        User.cant_login += 1
        print('User created')

    def full_name(self):
        return f'{self.nombre } {self.apellido}'

    # It is like toString java's method
    def __repr__(self):
        return f"{self.nombre} {self.apellido}"


user = User("Christian", "Altamirano")
print(user.nombre)
print(user.full_name())
print(User.cant_login)

user2 = User("Erik", "Anddy")
print(User.cant_login)

User.display_users_active()

print(user)
