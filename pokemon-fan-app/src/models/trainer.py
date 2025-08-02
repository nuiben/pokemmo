class Trainer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.roster = []
        self.party = []

    def add_to_roster(self, pokemon):
        self.roster.append(pokemon)

    def remove_from_roster(self, pokemon):
        if pokemon in self.roster:
            self.roster.remove(pokemon)

    def set_party(self, party):
        if len(party) <= 6:
            self.party = party
        else:
            raise ValueError("Party can only contain up to 6 Pokémon.")

    def get_roster(self):
        return self.roster

    def get_party(self):
        return self.party

    def __str__(self):
        return f"Trainer(username={self.username}, roster_size={len(self.roster)}, party_size={len(self.party)})"