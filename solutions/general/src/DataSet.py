import pandas as pd


class DataSet:
    def __init__(self, data):
        self._data = pd.DataFrame(data)

    def is_empty(self):
        return len(self._data) == 0

    def get_column_names(self):
        return list(self._data.columns)

    def get_data(self):
        return self._data.to_dict(orient='list')

    def create_difference_column(self, name, columns):
        """
        extend the dataset by another column, based on existing columns
        :param name: str name of the new column
        :param columns: list of existing columns for the operation
        """
        assert not (self.is_empty()), 'Cannot create column from others in an empty dataset'

        self._data[name] = self._data[columns[0]] - self._data[columns[1]]
