def get_daily_region():
    import requests

    # Fetch the current daily region from the PokeAPI
    response = requests.get("https://pokeapi.co/api/v2/region/daily")
    
    if response.status_code == 200:
        return response.json()
    else:
        return None