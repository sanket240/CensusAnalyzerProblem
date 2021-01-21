import pytest
from census_analyzer_exception import CensusAnalyzerException
from census_analyzer_header import CensusAnalyzerHeader
import pytest



# Test Case 1.1-To ensure the number of records
@pytest.mark.parametrize("actual", [30, 29, 27, 28])
def test_check_file_record(census_analyzer, actual):
    assert census_analyzer.get_count("./IndiaStateCensusData.csv") == actual



# Test Case 1.3-file is correct but the file type is incorrect returns exception
@pytest.mark.parametrize("actual",
                         ["./IndiaStateCensusData.txt", "./IndianStateCensusData.jpg", "./IndianStateCensusData.exe",
                          "./IndianStateCensusData.bak"])
def test_wrong_file_type(census_analyzer, actual):
    with pytest.raises(CensusAnalyzerException):
        census_analyzer.get_count(actual,2)


# Test Case 1.2-if file path is incorrect return a custom Exception
@pytest.mark.parametrize("actual", ["C:\IndiaStateCensusData.csv", "D:\programfiles\IndiaStateCensusData.csv",
                                    "C:\sanket\IndiaStateCensusData.csv"])
def test_check_wrong_file_path(census_analyzer, actual):
    with pytest.raises(CensusAnalyzerException):
        census_analyzer.get_count(actual,1)



# Test case 1.4-file is correct but delimiter incorrect return exception
@pytest.mark.parametrize("actual",
                         ["./IndiaStateCensusWrongDelimiter.csv", "./StateCensus.csv", "./IndiaStateCensusDelimiter.csv"])
def test_wrong_file_delimiter(census_analyzer, actual):
    with pytest.raises(CensusAnalyzerException):
        census_analyzer.get_count(actual,3)


# Test Case 1.5-To ensure the correct header
def test_csv_header():
    csv_header = CensusAnalyzerHeader()
    assert f'{csv_header}' == 'State,Population,AreaInSqKm,DensityPerSqKm'
