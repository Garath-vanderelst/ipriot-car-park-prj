import unittest
from sensor import Sensor
from sensor import EntrySensor
from sensor import ExitSensor
from car_park import CarPark
from random import randint

class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark('123 Fake St', 100)
        self.sensor = EntrySensor(1,True, self.car_park)


    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, EntrySensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, True)
        self.assertEqual(self.sensor.usage(), 'Entry')

    def test_scan_plate(self):
        self.assertTrue(self.sensor._scan_plate().startswith('FAKE'))

    def test_update_car_park(self):
        self.sensor.update_car_park('FAKE-001')
        self.assertIn('FAKE-001', self.car_park.plates)

    def test_detect_vehicle(self):
        previous_length = len(self.car_park.plates)
        self.sensor.detect_vehicle()
        current_length = len(self.car_park.plates)
        self.assertEqual(previous_length + 1, current_length)

class TestExitSensor(unittest.TestCase):
        def setUp(self):
            self.car_park = CarPark('123 Fake St', 100)
            self.sensor = ExitSensor(2, True, self.car_park)
            self.car_park.plates = ['FAKE-101', 'FAKE-102']

        def test_sensor_initialized_with_all_attributes(self):
            self.assertIsInstance(self.sensor, ExitSensor)
            self.assertEqual(self.sensor.id, 2)
            self.assertEqual(self.sensor.is_active, True)
            self.assertEqual(self.sensor.usage(), 'Exit')

        def test_scan_plate(self):
            exiting_car = self.sensor._scan_plate()
            self.assertIn(exiting_car, self.car_park.plates)

        def test_update_car_park(self):
            self.sensor.update_car_park('FAKE-101')
            self.assertNotIn('FAKE-101', self.car_park.plates)

