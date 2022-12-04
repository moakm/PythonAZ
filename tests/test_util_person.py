from unittest import TestCase


class TestBMI(TestCase):
    def test_calculate_bmi(self):
        # aarange
        from lib.utils.util_person import calculateBMI

        # act
        result = calculateBMI(1.7, 80.3)

        # assert
        self.assertGreater(result, 25)

    def test_gender(self):
        from lib.utils.util_person import gender

        result = gender('12121212345')

        self.assertEqual(result, 'W')