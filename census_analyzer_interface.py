import abc


class CensusAnalyzerMethods(abc.ABC):
    @abc.abstractmethod
    def get_count(self, file_path):
        pass

