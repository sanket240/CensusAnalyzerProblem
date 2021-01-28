import pytest
from census_analyzer_exception import CensusAnalyzerException
from census_analyzer_header import CensusAnalyzerHeader
import pytest

# Test Case 1.1-To ensure the number of records
@pytest.mark.parametrize("actual", [29,39,30,21])
def test_check_file_record(census_analyzer, actual):
    assert census_analyzer.get_count("IndiaStateCensusData.csv") == actual

# Test Case 1.3-file is correct but the file type is incorrect returns exception
@pytest.mark.parametrize("actual",
                         ["IndiaStateCensusData.txt", "IndiaStateCensusData.jpg", "IndiaStateCensusData.exe",
                          "IndiaStateCensusData.bak"])
def test_wrong_file_type(census_analyzer, actual):
    with pytest.raises(CensusAnalyzerException):
        census_analyzer.get_count(actual)

# Test Case 1.2-if file path is incorrect return a custom Exception
@pytest.mark.parametrize("actual", ["C:\IndiaStateCensusData.csv", "D:\programfiles\IndiaStateCensusData.csv",
                                    "C:\sanket\IndiaStateCensusData.csv"])
def test_check_wrong_file_path(census_analyzer, actual):
    with pytest.raises(CensusAnalyzerException):
        census_analyzer.get_count(actual)

# Test Case 1.4-To ensure the correct header
def test_csv_header():
    csv_header = CensusAnalyzerHeader()
    assert f'{csv_header}' == 'State,Population,AreaInSqKm,DensityPerSqKm'

def test_sort_by_area(census_analyzer):
    assert census_analyzer.sort_by_area() == True

def test_sort_by_population(census_analyzer):
    census_analyzer.sort_by_population() == True

def test_sort_by_population_density(census_analyzer):
    census_analyzer.sort_by_population_density() == True

def test_sort_by_state_code(census_analyzer):
    census_analyzer.sort_by_state_code() == True

def test_sort_by_state_name(census_analyzer):
    census_analyzer.sort_by_state_name() == True