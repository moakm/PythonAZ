from unittest import TestCase
from lib.classes.worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker1 = Worker('A', 'B', '121212123456', "IT", 'specjalista IT', 12345)

    def test_department(self):
        # assert
        self.assertEqual(self.worker1.department, "IT")

    def test_job(self):
        self.assertEqual(self.worker1.job, 'specjalista IT')

    def test_pesel(self):
        self.assertEqual(self.worker1.gender, 'W')

