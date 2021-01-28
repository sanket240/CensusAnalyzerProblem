from census_analyzer import CensusAnalyzer
import  pytest
import os.path


@pytest.fixture
def census_analyzer():
    obj = CensusAnalyzer()
    return obj
