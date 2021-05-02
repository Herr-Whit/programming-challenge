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
