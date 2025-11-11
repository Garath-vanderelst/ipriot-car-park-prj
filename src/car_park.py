from display import Display
from sensor import Sensor

class CarPark:
    def __init__(self, location: str, capacity: int, plates = None, displays = None, sensors = None):
        self.location = location
        self.capacity = capacity
        self.__plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []

    def __str__(self):
        return f'Car park at {self.location}, with {self.capacity} bays.'

    def register(component):
        """
        Registers Sensors and Displays
        :return:
        """
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a sensor or display")
        if isinstance(component) = Sensor:
            self.sensors.append(component)
        else:
            self.displays.append(component)


    def add_car(self, plate):
        """
        Adds a plate to the list of plates
        :param plate:
        :return:
        """
        self.__plates.append(plate)

    def remove_car():

    def update_displays():