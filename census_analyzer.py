import pandas as pd
import os.path
from census_analyzer_exception import CensusAnalyzerException
from census_analyzer_header import CensusAnalyzerHeader
from census_analyzer_state_code import CensusAnalyzerStateCode
from census_analyzer_interface import CensusAnalyzerMethods
import csv
import logging
indian_census_data ='IndiaStateCensusData'
indian_state_code='IndiaStateCode'

# Generates log in file named app.log
#Todo add line number
#Todo add log folder
logging.basicConfig(filename='log/app.log', format='%(levelname)s- %(message)s -%(asctime)s -%(lineno)d', level=logging.WARNING)

class CensusAnalyzer(CensusAnalyzerMethods):
    def __init__(self):
        pass
    # Method return records in file
    def get_count(self, file_path):
        '''
        Returns total number of records in file if file not present generates exception
            Parameters:
                file_path:file name and its location
        Returns:
                len(data): total number of records present in file
        '''
        file_name = os.path.splitext(file_path)[0]
        file_extension = os.path.splitext(file_path)[1]
        print(file_name)
        print(file_extension)
        if file_name != indian_state_code and file_name != indian_census_data:
            logging.warning("Wrong File Name")
            raise CensusAnalyzerException("Wrong File Name")

        elif f'{file_extension}' != '.csv':
            logging.warning("Wrong File Type")
            raise CensusAnalyzerException("Wrong File Type")
        else:
            col_names = repr(CensusAnalyzerStateCode()).split(",")
            col_names1 = repr(CensusAnalyzerHeader()).split(",")

            data = pd.read_csv(file_path, usecols=col_names1)
            r = csv.reader(open(file_path))
            lines = list(r)
            for i in range(len(lines)):
                print(lines[i])
            return len(data)

    # Method to sort data by state name
    def sort_by_state_name(self):
        '''
               Sort the data the in csv file by state name and convert that data into json file

        '''
        try:
            df = pd.read_csv("temp_data.csv")
            df.sort_values(by=['State Name'], inplace=True)
            print(df)
            df.to_json('json_file_sorted_by_state_name.json')
            return True
        except:
            raise CensusAnalyzerException('IO Error')

    # Method to sort data by state code
    def sort_by_state_code(self):
        '''
                Sort the data the in csv file by state code and convert that data into json file

        '''
        try:
            df = pd.read_csv("temp_data.csv")
            df.sort_values(by=['StateCode'], inplace=True)
            print(df)
            df.to_json('json_file_sorted_by_state_code.json')
            return True
        except:
            raise CensusAnalyzerException('IO Error')

    # Method to sort data by population
    def sort_by_population(self):
        '''
                Sort the data the in csv file by population and convert that data into json file

        '''
        try:
            df = pd.read_csv("temp_data1.csv")
            df.sort_values(by=['Population'], inplace=True)
            print(df)
            df.to_json('json_file_sorted_by_population.json')
            return True
        except:
            raise CensusAnalyzerException('IO Error')

    # Method to sort data by population dendity
    def sort_by_population_density(self):
        '''
                Sort the data the in csv file by population density and convert that data into json file

        '''
        try:
            df = pd.read_csv("temp_data1.csv")
            df.sort_values(by=['DensityPerSqKm'], inplace=True)
            print(df)
            df.to_json('json_file_sorted_by_population_density.json')
            return True
        except:
            raise CensusAnalyzerException('IO Error')

#Todo add test cases for sorting
    # Method to sort data by area in sq km
    def sort_by_area(self):
        '''
                Sort the data the in csv file by area and convert that data into json file

        '''
        try:
            df = pd.read_csv("temp_data1.csv")
            df.sort_values(by=['AreaInSqKm'], inplace=True,ascending=False)
            print(df)
            df.to_json('json_file_sorted_by_area.json')
            return True
        except:
            raise CensusAnalyzerException('IO Error')


    def read_data_into_dictionary(self):
        '''
                 Read data the from csv file and covert that data into dictionary

        '''
        input_file_state_code = csv.DictReader(open('IndiaStateCode.csv'))
        dict_state_code = {elem: [] for elem in input_file_state_code.fieldnames}
        for row in input_file_state_code:
            for key in dict_state_code.keys():
                dict_state_code[key].append(row[key])

        input_file_state_census_data = csv.DictReader(open('IndiaStateCensusData.csv'))
        dict_state_census_data = {elem: [] for elem in input_file_state_census_data.fieldnames}
        for row in input_file_state_census_data:
            for key in dict_state_census_data.keys():
                dict_state_census_data[key].append(row[key])
        print(dict_state_code)
        print(dict_state_census_data)


if __name__ == '__main__':
    state = CensusAnalyzer()
    #state.get_count("IndiaStateCensusData.csv")
    #state.read_data_into_dictionary()
    #state.sort_by_state_code()
    #state.sort_by_state_name()
    #state.sort_by_population()
    #state.read_data_into_dictionary()
    state.sort_by_population_density()
    #state.sort_by_area()
