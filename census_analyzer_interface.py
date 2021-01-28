import abc


class CensusAnalyzerMethods(abc.ABC):
    @abc.abstractmethod
    def get_count(self, file_path):
        pass

    @abc.abstractmethod
    def sort_by_state_name(self):
        pass

    @abc.abstractmethod
    def sort_by_state_code(self):
        pass

    @abc.abstractmethod
    def sort_by_population(self):
        pass

    @abc.abstractmethod
    def sort_by_population_density(self):
        pass

    @abc.abstractmethod
    def sort_by_area(self):
        pass

    @abc.abstractmethod
    def read_data_into_dictionary(self):
        pass