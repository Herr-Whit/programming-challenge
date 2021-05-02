import pandas as pd


class DataSet:
    def __init__(self, data):
        self._data = pd.DataFrame(data)

    def is_empty(self):
        return len(self._data) == 0

    def get_column_names(self):
        return list(self._data.columns)

    def create_column_from_others(self):
        raise AssertionError
