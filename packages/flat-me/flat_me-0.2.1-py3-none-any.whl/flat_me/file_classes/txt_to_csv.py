"""This module handles conversions from .txt files to .csv files"""
from .txt_utils import TxtUtils

class TxtToCsv(TxtUtils):
    """Create an object that handles txt to pandas convertion"""
    def __init__(self,path,header,delim,dest_extension):
        TxtUtils.__init__(self,path,header,delim,dest_extension)


    def return_file(self,df):
        """creating the desired file in the same directory as the old one"""
        print("Creating csv in the specified path")
        try:
            csv_path = self.path.replace('.txt','.csv')
            df.to_csv(csv_path,encoding='utf-8',index=False)
            print("Process completed, enjoy your new file(s)!")
        except ValueError as value_error:
            raise ValueError("Something went terribly wrong when returning the csv!") from value_error
