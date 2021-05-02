from abc import abstractmethod, abstractproperty, ABCMeta, ABC

import pandas as pd

from solutions.general.src.DataSet import DataSet


class DataFactory(ABC):
    @abstractmethod
    def load_data(self, **params):
        pass


class FileDataFactory(DataFactory):
    def __init__(self):
        pass

    def load_data(self, path):
        pd.read_csv(path)
        data = {}
        return DataSet(data)