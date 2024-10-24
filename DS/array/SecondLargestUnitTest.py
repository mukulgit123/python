import unittest
from SecondLargestInAnArray import secondLargest, secondSmallest


class TestSecondLargestInAnArray(unittest.TestCase):

    def test_second_largest(self):
        self.assertEqual(secondLargest(
            [1, 2, 4, 7, 7, 5, 19, 13, 16, 15]), 16, "Failed on array [1,2,4,7,7,5,19,13,16,15]")
        self.assertEqual(secondLargest(
            [1, 2, 3, 4, 5]), 4, "Failed on array [1,2,3,4,5]")
        self.assertEqual(secondLargest(
            [5, 4, 3, 2, 1]), 4, "Failed on array [5,4,3,2,1]")
        self.assertEqual(secondLargest(
            [1, 1, 1, 1, 1]), -1e9, "Failed on array [1,1,1,1,1]")

    def test_second_smallest(self):
        self.assertEqual(secondSmallest(
            [1, 2, 4, 7, 7, 5, 19, 13, 16, 15]), 2, "Failed on array [1,2,4,7,7,5,19,13,16,15]")
        self.assertEqual(secondSmallest(
            [1, 2, 3, 4, 5]), 2, "Failed on array [1,2,3,4,5]")
        self.assertEqual(secondSmallest(
            [5, 4, 3, 2, 1]), 2, "Failed on array [5,4,3,2,1]")
        self.assertEqual(secondSmallest(
            [1, 1, 1, 1, 1]), 1e9, "Failed on array [1,1,1,1,1]")


if __name__ == '__main__':
    unittest.main()
