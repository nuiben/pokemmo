import requests

class PokeAPIClient:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2"

    def fetch_pokemon(self, pokemon_name):
        response = requests.get(f"{self.base_url}/pokemon/{pokemon_name}")
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def fetch_region(self, region_name):
        response = requests.get(f"{self.base_url}/region/{region_name}")
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def catch_pokemon(self, pokemon_name):
        # Logic to simulate catching a Pokémon
        pokemon = self.fetch_pokemon(pokemon_name)
        if pokemon:
            return f"Caught {pokemon['name']}!"
        else:
            return "Failed to catch Pokémon."
