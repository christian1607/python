class User:

    #Class variable
    cant_login = 0

    @classmethod
    def display_users_active(cls):
        print(cls.cant_login)

    def __init__(self, name, last_name=''):
        self._nombre = name
        self._apellido = last_name
        User.cant_login += 1
        print('User created')

    def full_name(self):
        return f'{self.nombre } {self._apellido}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, name):
        self._nombre = name

    # It is like toString java's method
    def __repr__(self):
        return f"{self.nombre} {self._apellido}"


user = User("Christian", "Altamirano")
print(user.nombre)

user._nombre = "Cr7"
print(user.nombre)

print(user.full_name())
print(User.cant_login)

user2 = User("Erik", "Anddy")
print(User.cant_login)

User.display_users_active()

print(user)

print(user2.nombre)
