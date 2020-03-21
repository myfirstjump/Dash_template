import pandas as pd

class DataReader(object):

    def __init__(self):
        pass

    def read_csv_data(self, path):

        data = pd.read_csv(path, header=0, index_col=0)

        return data