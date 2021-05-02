from unittest import TestCase

from solutions.general.src.DataFactory import FileDataFactory
from solutions.general.src.DataSet import DataSet


class TestFileDataFactory(TestCase):
    def test_initialization(self):
        FileDataFactory()

    def test_load_data_returns_DataSet(self):
        data_factory = FileDataFactory()
        data = data_factory.load_data()

        self.assertIsInstance(data, DataSet)


class TestDataSet(TestCase):
    def test_initialization(self):
        data = {
            'a': [1, 2, 3],
            'b': ['a', 'b', 'c']
        }
        DataSet(data)

    def test_is_empty(self):
        data = {}
        ds = DataSet(data)
        self.assertTrue(ds.isempty())

    def test_is_not_empty(self):
        data = {
            'a': [1, 2, 3],
            'b': ['a', 'b', 'c']
        }
        ds = DataSet(data)
        self.assertFalse(ds.isempty())
