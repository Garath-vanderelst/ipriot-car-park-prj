class Sensor:
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

class EntrySensor(Sensor):
    def usage(self):
        return 'Entry'

class ExitSensor(Sensor):
    def usage(self):
        return 'Exit'
    pass

