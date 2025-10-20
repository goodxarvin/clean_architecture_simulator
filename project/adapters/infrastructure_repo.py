from adapters.interface_repo import AnimalInterfaceRepo
from entities.entity_info import Animal


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
