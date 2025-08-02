class Pokemon:
    def __init__(self, name, poke_type, abilities):
        self.name = name
        self.poke_type = poke_type
        self.abilities = abilities

    def get_info(self):
        return {
            "name": self.name,
            "type": self.poke_type,
            "abilities": self.abilities
        }

    def __str__(self):
        return f"{self.name} (Type: {self.poke_type})"