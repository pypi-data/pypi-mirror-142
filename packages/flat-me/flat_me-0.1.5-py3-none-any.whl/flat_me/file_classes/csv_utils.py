from os.path import exists
import pandas as pd
import sys

class CsvUtils:
    def __init__(self,path,header,delim,dest_extension,cur_extension='.csv'):
        self.path = path
        self.header = header
        self.dest_extension = dest_extension
        self.cur_extension = cur_extension

        if len(delim)==0:
            self.delim=","
        elif delim.lower() =='tab':
            self.delim='\t'
        else:
            self.delim = delim

    def validate_file(self):
        """Validating if the file is in the correct format"""
        if exists(self.path) and self.path.endswith('.csv'):
            return True
        raise FileNotFoundError("Either the path doesn't exist or the file is not a .csv")

    def retur_pd(self):
        """Return pandas DF for txt files"""
        final_header = None
        if self.header is True:
            final_header = 0

        if self.validate_file():
            try:
                df = pd.read_csv(self.path, sep=self.delim, header=final_header,engine='python',encoding_errors='replace')
                return df
            except UnicodeDecodeError:
                print("Something went really wrong with the encoding of your file!")
                raise UnicodeDecodeError
            except Exception:
                print("Unexpected error: ", sys.exc_info()[0])
                raise
