"""Creates a file object depending on answer to second CLI prompt"""
from .file_classes import CsvToTxt,TxtToCsv,CsvToJson, TxtToJson


class FileFactory():

    @staticmethod
    def create_file(format_chosen, answer, path):
        if format_chosen =='TXT to CSV':
            return TxtToCsv(path,answer['header_conf'],answer['delimeter'],".csv")
        if format_chosen == 'TXT to JSON':
            return TxtToJson(path,answer['header_conf'],answer['delimeter'],".json")
        if format_chosen =='CSV to TXT':
            return  CsvToTxt(path,answer['header_conf'],answer['delimeter'],".txt")
        if format_chosen=='CSV to JSON':
            return  CsvToJson(path,answer['header_conf'],answer['delimeter'],".json")
