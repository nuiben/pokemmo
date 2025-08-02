def catch_pokemon(trainer, pokeapi_client):
    daily_region = pokeapi_client.fetch_region()
    available_pokemon = pokeapi_client.fetch_pokemon(daily_region)

    if not available_pokemon:
        return "No Pokémon available to catch in the daily region."

    caught_pokemon = available_pokemon[0]  # Simulate catching the first available Pokémon
    trainer.roster.add(caught_pokemon)

    return f"{trainer.username} caught a {caught_pokemon.name}!"