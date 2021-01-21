import pandas as pd
from census_analyzer_exception import CensusAnalyzerException
from census_analyzer_header import CensusAnalyzerHeader
from census_analyzer_header import CensusAnalyzerHeader
from census_analyzer_state_code import CensusAnalyzerStateCode
from census_analyzer_interface import CensusAnalyzerMethods
import csv


class CensusAnalyzer(CensusAnalyzerMethods):
    def __init__(self):
        pass
    # Method return records in file
    def get_count(self, file_path,type):
        '''
        Returns total number of records in file if file not present generates exception
            Parameters:
                file_path:file name and its location
                type:type of exception it may generate
            Returns:
                len(data): total number of records present in file
        '''
        try:
            col_names = repr(CensusAnalyzerStateCode()).split(",")
            data = pd.read_csv(file_path, usecols=col_names)
            r = csv.reader(open(file_path))
            lines = list(r)
            for i in range(len(lines)):
                print(lines[i])
            return len(data)

        except IOError:
            message = self.get_exception_type(type)
            logging.warning(message)
            raise CensusAnalyzerException(message)
        except Exception as e:
            print(str(e))

    # Method return type of exception
    def get_exception_type(self, value):
        switcher = {
            1: "Wrong File Name", 2:"Wrong File Type",  3: "Wrong Delimiter",0:"None"
        }
        return switcher.get(value, "hi")


if __name__ == '__main__':
    state = CensusAnalyzer()
    print(state.get_count("IndiaStateCode.csv",0))
