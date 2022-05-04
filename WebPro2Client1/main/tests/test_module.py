from unittest import TestCase
from ..models import Module1


class UnitTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData: done')
        pass

    def setUp(self):
        print('setUp: done')
        pass

    def test_is_false(self):
        print('Method false: done')
        self.assertFalse(False)

    def test_is_true(self):
        post=Module1()
        self.assertTrue(post.get_num())

    def test_is_add(self):
        print('Method add: done')
        self.assertEqual(12+12, 24)

    def test_is_multiple(self):
        print('Method multiply: done')
        self.assertEqual(11*11, 121)
