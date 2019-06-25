from unittest import TestCase
import task52


class TestTask5(TestCase):

    def setUp(self):
        """Init"""

    def test_task5(self):
        self.assertFalse(task52.letter("p"))
        self.assertTrue(task52.letter("k"))

    def tearDown(self):
        """Finish"""
