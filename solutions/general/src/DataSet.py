import pandas as pd


class DataSet:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def is_empty(self):
        return len(self.data) == 0