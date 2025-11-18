import unittest
from sensor import Sensor
from sensor import EntrySensor
from sensor import ExitSensor
from car_park import CarPark
from random import randint

class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.sensor = EntrySensor(1,True, CarPark('123 Fake St', 100))

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, EntrySensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, True)
        self.assertEqual(self.sensor.usage, 'Entry')

    def test_scan_plate(self):
        self.assertEqual(self.sensor._scan_plate().startswith('FAKE'), True)

    def test_update_car_park(self):
        self.sensor.update_car_park('FAKE-001')
        #TODO Work out how to test this and the next

    def test_detect_vehicle(self):
        self.sensor.detect_vehicle()


class TestExitSensor(unittest.TestCase):
        def setUp(self):
            self.sensor = ExitSensor(2, True, CarPark('123 Fake St', 100))

        def test_sensor_initialized_with_all_attributes(self):
            self.assertIsInstance(self.sensor, ExitSensor)
            self.assertEqual(self.sensor.id, 2)
            self.assertEqual(self.sensor.is_active, True)
            self.assertEqual(self.sensor.usage, 'Exit')

        def test_scan_plate(self):
            self.car_park.plates = ['FAKE-101']
            self.assertEqual(self.sensor._scan_plate() in self.car_park.plates, True)

        def test_update_car_park(self):
            self.sensor.update_car_park('FAKE-001')
            # TODO Work out how to test this and the previous

