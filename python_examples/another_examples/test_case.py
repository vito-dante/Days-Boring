import unittest
from total_value_sum import total_sum
from total_value_sum import example_boolean
from total_value_sum import total_sum_best_way
from exercise import exchange_letter
from exercise import order_bubble_sort
from prime import prime
from number_digits import numbers_digit

class Test_Exercise(unittest.TestCase):

    DISABLE_TEST = True

    @unittest.skipIf(DISABLE_TEST, "message all test disable")
    def test_sum_total(self) -> None:
        self.assertEqual(total_sum(range(11)), 30)

    @unittest.skipIf(DISABLE_TEST, "message all test disable")
    def test_true_reverse(self) -> None:
        assert example_boolean(True) == False

    @unittest.skipIf(DISABLE_TEST, "message all test disable")
    def test_lambda(self) -> None:
        self.assertEqual(total_sum_best_way(range(10)), 20)

    @unittest.skipIf(DISABLE_TEST, "message all test disable")
    def test_exchange_letter(self) -> None:
        self.assertEqual(exchange_letter("hello vito ooo", "o","a"),
                         "hella vita aaa" )

    @unittest.skipIf(DISABLE_TEST, "message all test disable")
    def test_order_bubble_sort(self) -> None:
        self.assertEqual(order_bubble_sort([32,4,545,5,46,2,21,3]),
                         [2,3,4,5,21,32,46,545])

    @unittest.skipIf(DISABLE_TEST, "message all test disable")
    def test_prime(self) -> None:
        self.assertEqual(list(prime(13)),[1,2,3,5,7,11,13])

    def test_numbers_digit(self) -> None:
        self.assertEqual(numbers_digit(78945),5)

if __name__ == '__main__':
    unittest.main()
