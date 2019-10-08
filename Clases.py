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
person.talk();