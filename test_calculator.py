
# https://github.com/notfeardan/lab11-DB-PB
# Partner 1: Daniil Baturyn
# Partner 2: Pavel Baturyn
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(2, 10), 5.0)
        self.assertAlmostEqual(div(5, 25), 5.0)
        self.assertAlmostEqual(div(-2, 8), -4.0)
    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -5)  # invalid argument (b <= 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-6, -8), 10.0)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(4), 2.0)
        self.assertAlmostEqual(square_root(9), 3.0)
        with self.assertRaises(ValueError):
            square_root(-1)  # invalid argument (a < 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
