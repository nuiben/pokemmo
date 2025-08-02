class Roster:
    def __init__(self):
        self.pokemon_list = []

    def add_pokemon(self, pokemon):
        self.pokemon_list.append(pokemon)

    def remove_pokemon(self, pokemon):
        if pokemon in self.pokemon_list:
            self.pokemon_list.remove(pokemon)

    def list_pokemon(self):
        return self.pokemon_list

    def get_pokemon_count(self):
        return len(self.pokemon_list)