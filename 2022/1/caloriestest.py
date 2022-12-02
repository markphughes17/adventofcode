import unittest


class MyTestCase(unittest.TestCase):
    def test_totalCaloriesOfMostBurdenedElf(self):
        self.assertEquals(self.totalCals, 42,619)  # add assertion here


if __name__ == '__main__':
    unittest.main()
