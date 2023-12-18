class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        Stop the car
        """
        return "%s braking" % self.vtype

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving a %s %s!" % (self.color, self.vtype)

    def drift(self):
        "Drift the car"
        return "I'm drifting a %s %s" % (self.color)


class Car(Vehicle):
    """
    The Car class
    """

    # ----------------------------------------------------------------------
    def brake(self):
        """
        Override brake method
        """
        return "The %s is breaking slowly!" % (self.vtype)


if __name__ == "__main__":
    car = Car("yellow", 2, 4, "car")
    print(car.brake())
    'The car class is breaking slowly!'
    car.drive()
    "I'm driving a yellow car!"

if __name__ == "__main__":
    driftcar = Vehicle("black", 2, 4, "driftcar")
    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("green", 3, 6, "truck")
    print(driftcar.drive())
    print(truck.brake())

