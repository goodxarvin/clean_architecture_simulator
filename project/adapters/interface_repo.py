from abc import ABC, abstractmethod


class AnimalInterfaceRepo(ABC):
    @abstractmethod
    def get_all_animals(self):
        pass

    @abstractmethod
    def add_animal(self, name, age, species):
        pass

    @abstractmethod
    def filter_animal(self, name=None, age=None, species=None):
        pass
