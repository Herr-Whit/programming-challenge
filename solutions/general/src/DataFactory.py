from abc import abstractmethod, ABC
import pandas as pd
from solutions.general.src.DataSet import DataSet


class DataFactory(ABC):
    @abstractmethod
    def load_data(self, **params):
        pass


def load_csv(path):
    df = pd.read_csv(path)
    data = df.to_dict(orient='list')
    return data


class FileDataFactory(DataFactory):
    loading_collection = {
        'csv': load_csv
    }

    def __init__(self):
        pass

    def load_data(self, path):
        """
        load data from file
        :param path: string indicating a file path
        :return: DataSet object containing the file data.
        """
        file_type = path.split('.')[-1]
        data = self.loading_collection[file_type](path)
        return DataSet(data)
