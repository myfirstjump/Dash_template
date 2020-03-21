import os

import pandas as pd
from py_module.config import Configuration
from py_module.data_reader import DataReader
from py_module.dash_builder import DashBuilder

class CLASSPLACEHOLDER(object):

    def __init__(self):
        self.config_obj = Configuration()
        self.reader_obj = DataReader()
    
    def data_loading(self):
        file_path = os.path.join(self.config_obj.data_folder, self.config_obj.file_name)
        data = self.reader_obj.read_csv_data(file_path)
        return data

    def dash_server(self):
        self.dash_app = DashBuilder()

def PLACEHOLDER_main():
    main_obj = CLASSPLACEHOLDER()
    data = main_obj.data_loading()
    main_obj.dash_server() # Run dash server

if __name__ == "__main__":
    PLACEHOLDER_main()