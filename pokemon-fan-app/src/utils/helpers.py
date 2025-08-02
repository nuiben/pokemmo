def validate_username(username):
    if len(username) < 3:
        raise ValueError("Username must be at least 3 characters long.")
    return True

def validate_password(password):
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long.")
    return True

def format_pokemon_name(name):
    return name.capitalize()

def format_trainer_name(name):
    return name.strip().title()