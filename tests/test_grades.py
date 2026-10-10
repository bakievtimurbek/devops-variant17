import unittest

from grades import average_score


class AverageScoreTests(unittest.TestCase):
    def test_average_of_three_scores(self):
        self.assertEqual(average_score([80, 90, 100]), 90)

    def test_single_score(self):
        self.assertEqual(average_score([75]), 75)

    def test_boundary_scores(self):
        self.assertEqual(average_score([0, 100]), 50)

    def test_rounding(self):
        self.assertEqual(average_score([80, 81, 81]), 80.67)

    def test_empty_list_is_rejected(self):
        with self.assertRaises(ValueError):
            average_score([])

    def test_out_of_range_is_rejected(self):
        for score in [-1, 101]:
            with self.subTest(score=score), self.assertRaises(ValueError):
                average_score([score])

    def test_invalid_types_are_rejected(self):
        for score in ["90", None, True]:
            with self.subTest(score=score), self.assertRaises(ValueError):
                average_score([score])

    def test_nonfinite_numbers_are_rejected(self):
        for score in [float("nan"), float("inf"), float("-inf")]:
            with self.subTest(score=score), self.assertRaises(ValueError):
                average_score([score])


if __name__ == "__main__":
    unittest.main()
