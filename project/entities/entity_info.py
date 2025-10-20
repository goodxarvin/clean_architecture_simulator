class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def info(self):
        return {'name': self.name, 'age': self.age, 'species': self.species}
