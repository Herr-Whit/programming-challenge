from abc import abstractmethod, abstractproperty, ABCMeta, ABC


class DataFactory(ABC):
    @abstractmethod
    def load_data(self):
        pass


class FileDataFactory(DataFactory):
    def __init__(self):
        pass
    def load_data(self):
        pass