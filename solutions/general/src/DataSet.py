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

    def create_difference_column(self, column_name, columns):
        """
        extend the dataset by another column, based on existing columns
        :param column_name: str name of the new column
        :param columns: list of existing columns for the operation
        """
        assert not (self.is_empty()), 'Cannot create column from others in an empty dataset'

        self._data[column_name] = self._data[columns[0]] - self._data[columns[1]]

    def reduce_column(self, column_name, reduction):
        """
        reduce a column to a single value with the given reduction
        :param column_name: str name of the column
        :param reduction: function reducing array-like to single value
        :return: reduction result
        """
        assert not (self.is_empty()), 'Cannot reduce column in an empty dataset'
        return reduction(self._data[column_name])

    def get_max(self, column_name):
        assert not (self.is_empty()), 'Cannot find maximum in an empty dataset'
        maximum = self.reduce_column(column_name, max)
        max_rows = self._data[self._data[column_name] == maximum]
        return max_rows.to_dict(orient='list')

