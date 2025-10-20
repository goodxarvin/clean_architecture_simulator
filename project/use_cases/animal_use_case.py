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
