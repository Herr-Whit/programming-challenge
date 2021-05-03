from abc import abstractmethod, ABC
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
        """
        load data from file
        :param path: either pathlib.Path object or string indicating a file path
        :return: DataSet object containing the file data.
        """
        df = pd.read_csv(path)
        data = df.to_dict(orient='list')
        return DataSet(data)
