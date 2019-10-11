import utils
import repository.conexion

class Point:

    # Constructors, python support just one constructor per class,
    # but it allows you to define default values
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # methods
    def move(self):
        print("moving")
        print("moved")

    def draw(self):
        print("drawed")


point = Point()
point.draw()
point.move()
# This is possible with python
point.name = "circle"  # attribute is created

print(point.name)

point2 = Point(10, 20)
print(point2.x)





class Person:

    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hello {self.name}, have a nice day")


person=Person("christian")
person.talk()


#Usando metodo de otro archivo python
print("Suma: "+ str(utils.sumar(1,2)))


#usando llamada a metodo de un paquete creado
repository.conexion.obtener_conexion("admin","123456","192.168.1.100")
repository.conexion.cerrar_conexion()
