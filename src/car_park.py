from display import Display
from sensor import Sensor

class CarPark:
    def __init__(self, location: str, capacity: int, plates = None, displays = None, sensors = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []

    def __str__(self):
        return f'Car park at {self.location}, with {self.capacity} bays.'

    def register(self, component):
        """
        Registers Sensors and Displays
        :return:
        """
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a sensor or display")
        elif isinstance(component) = Sensor:
            self.sensors.append(component)
        else:
            self.displays.append(component)

    def add_car(self, plate):
        """
        Adds a plate to the list of plates after making sure its not already in there
        :param plate:
        :return:
        """
        if plate in self.plates:
            pass
        else:
            self.plates.append(plate)
            self.update_displays()

    def remove_car(self, plate):
        """
        Removes plate from list of plates
        :param plate:
        :return:
        """
        if plate not in self.plates:
            pass
        else:
            self.plates.remove(plate)
            self.update_displays()
#TODO Check the method for updating the display display.update()
    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 21}
        for display in self.displays:
            display.update(data)

    @property
    def available_bays(self):
        return (max(self.capacity - len(self.plates), 0))

