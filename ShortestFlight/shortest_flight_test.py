import unittest

from Algorithmic.ShortestFlight.shortest_flight import find_shortest_flight


class MyTestCase(unittest.TestCase):

    # Test case where the source and destination are the same city (output should be 0)
    def test_same_city(self):
        self.assertEqual(find_shortest_flight([['SOF', 'SOF']], 'SOF', 'SOF'), 0)

    # Test case where the source and destination are not connected by any flights (output should be 0)
    def test_unreachable(self):
        self.assertEqual(find_shortest_flight([['SOF', 'EIN'], ['NYC', 'MLE']], 'SOF', 'MLE'), 0)

    # Example 1 from the task
    # output should be 3
    def test_1(self):
        self.assertEqual(find_shortest_flight([['SOF', 'IST'], ['IST', 'CMB'], ['CMB', 'MLE']], 'SOF', 'MLE'), 3)

    # Example 2 from the task
    # output should be 1
    def test_2(self):
        self.assertEqual(find_shortest_flight([['SOF', 'MLE'], ['SOF', 'LON'], ['LON', 'MLE']], 'SOF', 'MLE'), 1)

    # Example 3 from the task
    # output should be 0
    def test_3(self):
        self.assertEqual(find_shortest_flight([['SOF', 'LON'], ['SOF', 'NYC']], 'SOF', 'MLE'), 0)

    def test_same_city2(self):
        self.assertEqual(find_shortest_flight([['SOF', 'SOF', 2]], 'SOF', 'SOF', 1), 0)

    # Test case where the source and destination are not connected by any flights (output should be 0)
    def test_unreachable2(self):
        self.assertEqual(find_shortest_flight([['SOF', 'EIN', 4], ['NYC', 'MLE', 2]], 'SOF', 'MLE', 2), 0)

    # Example 4 from the task
    # output should be 2
    def test_12(self):
        self.assertEqual(find_shortest_flight([['SOF', 'MLE', 2], ['SOF', 'LON', 3], ['LON', 'MLE', 4]], 'SOF',
                                                       'MLE', 3), 2)


if __name__ == '__main__':
    unittest.main()
