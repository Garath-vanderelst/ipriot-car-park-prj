from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


carpark = CarPark('moondalup', 100, log_file='moondalup.txt', json_file_name = 'moondalup_config.json')

carpark.write_config()

carpark.from_config('moondalup_config.json')

sensor1 = EntrySensor(1,True, carpark)

sensor2 = ExitSensor(2, True, carpark)

display1 = Display(1,'Welcome to Moondalup', True, carpark)

for car in range(10):
    sensor1.detect_vehicle()

for car in range(2):
    sensor2.detect_vehicle()