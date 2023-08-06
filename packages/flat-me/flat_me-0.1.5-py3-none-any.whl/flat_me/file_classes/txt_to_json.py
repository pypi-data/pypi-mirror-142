"""This module handles conversion from """
from .txt_utils import TxtUtils

class TxtToJson(TxtUtils):
    """Create an object that handles txt to pandas convertion"""
    def __init__(self, path, header, delim, dest_extension):
        TxtUtils.__init__(self, path, header, delim, dest_extension)

    def return_file(self,df):
        """creating the desired file in the same directory as the old one"""
        print("Creating csv in the specified path")
        try:
            json_path = self.path.replace('.txt', '.json')
            df.to_json(json_path, orient="columns")
            print("Process completed, enjoy your new file(s)!")
        except ValueError as value_error:
            raise ValueError("Something went terribly wrong when returning the json file!") from value_error