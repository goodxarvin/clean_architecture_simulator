from adapters.infrastructure_repo import AnimalInfrastructureRepo
from use_cases.animal_use_case import GetAllAnimals, AddAnimals, FilterAnimals


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
