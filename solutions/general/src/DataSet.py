import pandas as pd


class DataSet:
    def __init__(self, data):
        self._data = pd.DataFrame(data)

    def is_empty(self):
        """
        Check if the dataset is empty
        :return: boolean indicating emptiness
        """
        return len(self._data) == 0

    def get_column_names(self):
        """
        get the names of the columns of the datasets
        :return: list of strings of the dataset
        """
        return list(self._data.columns)

    def get_data(self):
        """
        get the dataset contents in native python data form
        :return: dictionary of lists with column names as keys
        """
        return self._data.to_dict(orient='list')

    def create_absolute_difference_column(self, column_name, columns):
        """
        extend the dataset by another column, based on existing columns
        :param column_name: str name of the new column
        :param columns: list of existing columns for the operation
        """
        assert not (self.is_empty()), 'Cannot create column from others in an empty dataset'

        self._data[column_name] = (self._data[columns[0]] - self._data[columns[1]]).abs()

    def reduce_column(self, column_name, reduction):
        """
        reduce a column to a single value with the given reduction
        :param column_name: str name of the column
        :param reduction: function reducing array-like to single value
        :return: reduction result
        """
        assert not (self.is_empty()), 'Cannot reduce column in an empty dataset'
        return reduction(self._data[column_name])

    def get_row_on_column_reduction(self, column_name, reduction):
        """
        get a row based, where the attribute matches a reduction (min/max/median) of the same column
        :param column_name: string indicating the column in question
        :param reduction: reduction function to
        :return: dictionary of lists with column names as keys containing rows matching the reduction result
        """
        assert not (self.is_empty()), 'Cannot find row in an empty dataset'
        maximum = self.reduce_column(column_name, reduction)
        max_rows = self._data[self._data[column_name] == maximum]
        return max_rows.to_dict(orient='list')

