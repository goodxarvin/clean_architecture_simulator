# entities/entity.py:

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def info(self):
        return {'name': self.name, 'age': self.age, 'species': self.species}


# adapters/interface_repo.py:

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


# adapters/infrastructure_repo.py:

from entities.entity_info import Animal
from adapters.interface_repo import AnimalInterfaceRepo

class AnimalInfrastructureRepo(AnimalInterfaceRepo):
    def __init__(self):
        self.animal_data = []

    def get_all_animals(self):
        all_animals = [{"name": animal_data.name, "age": animal_data.age, "species": animal_data.species} for animal_data in self.animal_data
                       ]
        return f"all animals:\n{all_animals}"

    def __get_animal_info(self):
        self.unfilter_data = []
        for animal in self.animal_data:
            animal_dict = {}
            animal_dict['name'] = animal.name
            animal_dict['age'] = animal.age
            animal_dict['species'] = animal.species
            self.unfilter_data.append(animal_dict)
        return self.unfilter_data

    def add_animal(self, name, age, species):
        self.animal_data.append(Animal(name, age, species))

    def filter_animal(self, name=None, age=None, species=None):
        unfiltered_data = self.__get_animal_info()
        filtered_data = []
        filters = {"name": name, "age": age, "species": species}
        filters = {k: v for k, v in filters.items() if v is not None}
        for filter_result in unfiltered_data:
            if all(filter_result[k] == filters[k] for k in filters):
                filtered_data.append(filter_result)

        return f"results: {filtered_data}" if filtered_data else "nothing found..."

# use_cases/use_case.py:


class GetAllAnimals:
    def __init__(self, repo):
        self.repo = repo

    def execute(self):
        return self.repo.get_all_animals()


class AddAnimals:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, name, age, species):
        return self.repo.add_animal(name, age, species)


class FilterAnimals:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, name=None, age=None, species=None):
        return self.repo.filter_animal(name, age, species)


# frameworks/framework.py

from use_cases.animal_use_case import GetAllAnimals, AddAnimals, FilterAnimals
from adapters.infrastructure_repo import AnimalInfrastructureRepo

class Main:
    animal_repo = AnimalInfrastructureRepo()

    def get_all_animals(self):
        animal_use_case_get_all = GetAllAnimals(self.animal_repo)
        return animal_use_case_get_all.execute()

    def add_animal(self, name, age, species):
        animal_use_case_add = AddAnimals(self.animal_repo)
        return animal_use_case_add.execute(name, age, species)

    def filter_animals(self, name=None, age=None, species=None):
        animal_use_case_filter = FilterAnimals(self.animal_repo)
        return animal_use_case_filter.execute(name, age, species)


if __name__ == "__main__":
    client = Main()
    client.add_animal("john", "3", "dog")
    client.add_animal("layla", "10", "cat")
    client.add_animal("milo", "20", "cat")
    client.add_animal("milo", "1", "dog")
    client.add_animal("merlin", "2", "crow")
    print(client.get_all_animals())
    print(client.filter_animals("milo"))
