class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth


def new_pet(pet_name: str, pet_species: str, pet_year: int):
    pet_ = Pet(pet_name, pet_species, pet_year)
    # pet_.name = pet_name
    # pet_.species = pet_species
    # pet_.year_of_birth = pet_year
    return pet_


if __name__ == '__main__':
    fluffy = new_pet("Fluffy", "dog", 2017)
    print(fluffy.name)
    print(fluffy.species)
    print(fluffy.year_of_birth)
