import unittest

from Algorithmic.ShortestFlight.shortest_flight import find_shortest_flight


class MyTestCase(unittest.TestCase):

    # Test case where the source and destination are the same city (output should be 0)
    def test_find_shortest_flight_when_same_city_returns_0(self):
        self.assertEqual(find_shortest_flight([['SOF', 'SOF']], 'SOF', 'SOF'), 0)

    # Test case where the source and destination are not connected by any flights (output should be 0)
    def test_find_shortest_flight_when_cities_not_connected_returns_0(self):
        self.assertEqual(find_shortest_flight([['SOF', 'EIN'], ['NYC', 'MLE']], 'SOF', 'MLE'), 0)

    # Example 1 from the task
    # output should be 3
    def test_find_shortest_flight_example_1_returns_3(self):
        self.assertEqual(find_shortest_flight([['SOF', 'IST'], ['IST', 'CMB'], ['CMB', 'MLE']], 'SOF', 'MLE'), 3)

    # Example 2 from the task
    # output should be 1
    def test_find_shortest_flight_example_2_returns_1(self):
        self.assertEqual(find_shortest_flight([['SOF', 'MLE'], ['SOF', 'LON'], ['LON', 'MLE']], 'SOF', 'MLE'), 1)

    # Example 3 from the task
    # output should be 0
    def test_find_shortest_flight_example_3_returns_0(self):
        self.assertEqual(find_shortest_flight([['SOF', 'LON'], ['SOF', 'NYC']], 'SOF', 'MLE'), 0)


if __name__ == '__main__':
    unittest.main()