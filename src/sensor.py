from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active or False
        self.car_park = car_park

    def __str__(self):
        if self.is_active == True:
            sensor_status = 'Active'
        else:
            sensor_status = 'Inactive'

        return f'{self.usage()}Sensor{self.id} at {self.car_park} is {sensor_status}'

    def _scan_plate(self):
        return 'FAKE' + format(random.randint(0,999), '03d')

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def detect_vehicle(self):
        plate_number = self._scan_plate()
        self.update_car_park(plate_number)

class EntrySensor(Sensor):
    def usage(self):
        return 'Entry'

    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f'Incoming car detected. Plate: {plate}')

class ExitSensor(Sensor):
    def usage(self):
        return 'Exit'

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)


