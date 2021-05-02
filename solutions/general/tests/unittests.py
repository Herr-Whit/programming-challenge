from operator import sub
from unittest import TestCase

from solutions.general.src.DataFactory import FileDataFactory
from solutions.general.src.DataSet import DataSet


class TestFileDataFactory(TestCase):
    def setUp(self) -> None:
        self.test_path = './test_files/test_small.csv'
        self.non_existing_path = './test_files/not_exist.csv'

    def test_initialization(self):
        FileDataFactory()

    def test_load_data_returns_DataSet(self):
        data_factory = FileDataFactory()
        data = data_factory.load_data(self.test_path)

        self.assertIsInstance(data, DataSet)


class TestDataSet(TestCase):
    def setUp(self) -> None:
        self.data = {
            'a': [1, 2, 3],
            'b': [4, 5, 6]
        }

    def test_initialization(self):
        DataSet(self.data)

    def test_is_empty(self):
        data = {}
        ds = DataSet(data)
        self.assertTrue(ds.is_empty())

    def test_is_not_empty(self):
        ds = DataSet(self.data)
        self.assertFalse(ds.is_empty())

    def test_get_column_names(self):
        ds = DataSet(self.data)

        column_names = ds.get_column_names()
        self.assertEqual(['a', 'b'], column_names)

    def test_create_difference_column_fails_if_empty(self):
        data = {}
        ds = DataSet(data)

        self.assertRaises(AssertionError, ds.create_difference_column, **{'name': '', 'columns': []})

    def test_get_data(self):
        ds = DataSet(self.data)
        self.assertEqual(self.data, ds.get_data())

    def test_create_difference_column(self):
        ds = DataSet(self.data)

        ds.create_difference_column('c', ['a', 'b'])
        column_names = ds.get_column_names()
        self.assertEqual(['a', 'b', 'c'], column_names)
        new_data = ds.get_data()
        self.assertEqual(self.data['a'][0] - self.data['b'][0], new_data['c'][0])

    def test_reduce_column_fails_if_empty(self):
        data = {}
        ds = DataSet(data)

        self.assertRaises(AssertionError, ds.reduce_column, **{'name': '', 'reduction': None})

    def test_reduce_column(self):
        ds = DataSet(self.data)

        a_max = ds.reduce_column('a', max)
        b_sum = ds.reduce_column('b', sum)

        self.assertEqual(3, a_max)
        self.assertEqual(15, b_sum)



