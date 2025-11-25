from display import Display
from sensor import Sensor
from pathlib import Path
from datetime import datetime
import json

class CarPark:
    def __init__(self, location: str, capacity: int, log_file = Path('log.txt'), plates = None, displays = None, sensors = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return f'Car park at {self.location}, with {self.capacity} bays.'

    def register(self, component):
        """
        Registers Sensors and Displays
        :return:
        """
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a sensor or display")
        elif isinstance(component) == Sensor:
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
            self._log_car_activity(plate, 'entered')

    def remove_car(self, plate):
        """
        Removes plate from list of plates
        :param plate:
        :return:
        """
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, 'exited')

#TODO Check the method for updating the display display.update()
    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 21}
        for display in self.displays:
            display.update(data)

    def _log_car_activity(self, plate, action):
        now = datetime.now()
        with open (self.log_file, 'a') as log:
            log.write(f'{plate} {action} {now}\n')

    def write_config(self):
        with open('config.json', 'w'):
            json.dump({'location': self.location,
                       'capacity': self.capacity,
                       'log_file': self.log_file}, f)

    @classmethod
    def from_config(cls, config_file=Path('config.json')):
        if isinstance(config_file, Path):
            config_file = config_file
        else:
            config_file = Path(config_file)
        with open(config_file, 'r') as json_file:
            config = json.load(json_file)

        return cls(config['location'], config['capacity'], log_file = config['log_file'])

    @property
    def available_bays(self):
        return (max(self.capacity - len(self.plates), 0))

