from abc import abstractmethod, abstractproperty, ABCMeta


class DataFactory:
    @abstractmethod
    def load_data(self):
        pass


class FileDataFactory(DataFactory):
    def __init__(self):
        pass