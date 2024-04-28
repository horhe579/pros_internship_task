import unittest

from Algorithmic.ShortestFlight.shortest_flight_subtask import find_shortest_flight_modified


class MyTestCase(unittest.TestCase):

    # Test case where the source and destination are the same city (output should be 0)
    def test_find_shortest_flight_when_same_city_returns_0(self):
        self.assertEqual(find_shortest_flight_modified([['SOF', 'SOF', 2]], 'SOF', 'SOF', 1), 0)

    # Test case where the source and destination are not connected by any flights (output should be 0)
    def test_find_shortest_flight_when_cities_not_connected_returns_0(self):
        self.assertEqual(find_shortest_flight_modified([['SOF', 'EIN', 4], ['NYC', 'MLE', 2]], 'SOF', 'MLE', 2), 0)

    # Example 4 from the task
    # output should be 2
    def test_find_shortest_flight_example_4_returns_2(self):
        self.assertEqual(find_shortest_flight_modified([['SOF', 'MLE', 2], ['SOF', 'LON', 3], ['LON', 'MLE', 4]], 'SOF',
                                                       'MLE', 3), 2)


if __name__ == '__main__':
    unittest.main()