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
    def setUp(self) -> None:
        self.data = {
            'a': [1, 2, 3],
            'b': ['a', 'b', 'c']
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
