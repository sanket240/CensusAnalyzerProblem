from state_census_analyzer import CensusAnalyzer

@pytest.fixture
def census_analyzer():
    obj = CensusAnalyzer()
    return obj
