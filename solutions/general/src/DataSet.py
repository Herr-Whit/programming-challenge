import pandas as pd


class DataSet:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def isempty(self):
        return True