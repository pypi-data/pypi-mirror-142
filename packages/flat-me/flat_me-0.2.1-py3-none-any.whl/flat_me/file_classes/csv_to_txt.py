"""This module handles conversions from .csv files to .txt files"""
from .csv_utils import CsvUtils

class CsvToTxt(CsvUtils):
    def __init__(self,path,header,delim,dest_extension):
        CsvUtils.__init__(self,path,header,delim,dest_extension)

    def return_file(self,df):
        """creating the desired file in the same directory as the old one"""
        print("Creating csv in the specified path...")
        try:
            txt_path = self.path.replace('.csv','.txt')
            df.to_csv(txt_path,header=self.header,index=False)
            print("Process completed, enjoy your new file(s)!")
        except ValueError as value_error:
            raise ValueError("Something went terribly wrong when returning the txt file!") from value_error
