def challenge_trainer(challenger, opponent):
    """
    Allows a trainer to challenge another trainer.
    
    Parameters:
    challenger (Trainer): The trainer initiating the challenge.
    opponent (Trainer): The trainer being challenged.
    
    Returns:
    str: Outcome of the challenge and rewards if applicable.
    """
    # Simulate a challenge outcome based on random chance
    import random
    
    challenger_power = sum(pokemon.power for pokemon in challenger.party)
    opponent_power = sum(pokemon.power for pokemon in opponent.party)
    
    if challenger_power > opponent_power:
        challenger.reward()
        return f"{challenger.username} wins the challenge against {opponent.username}!"
    elif challenger_power < opponent_power:
        return f"{opponent.username} wins the challenge against {challenger.username}!"
    else:
        return "It's a tie!"