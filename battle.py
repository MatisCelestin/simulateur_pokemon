import random

def calculate_damage(attacker, defender, move):
    """
    Calcule les dégâts infligés par un Pokémon (attacker) à un autre (defender)
    en utilisant un mouvement spécifique (move).
    """
    
    level = attacker.level
    power = move.power
    if move.category == "Physical":
        attack = attacker.attack
        defense = defender.defense
    elif move.category == "Special": 
        attack = attacker.special_attack
        defense = defender.special_defense
    else:
        return 0 

 
    damage = (((2 * level / 5 + 2) * power * attack / defense) / 50) + 2

    
    effectiveness = type_effectiveness(move.type, defender.type)
    damage *= effectiveness

    return int(damage)

def type_effectiveness(move_type, defender_type):
    """
    Calcule l'efficacité d'un mouvement en fonction de la faiblesse/résistance du défenseur.
    """
   
    type_chart = {
        ("Fire", "Grass"): 2, 
        ("Water", "Fire"): 2,  
        ("Water", "Electric"): 0.5, 
        ("Electric", "Water"): 2,  
        ("Fire", "Water"): 0.5,  
        ("Electric", "Ground"): 0,  
        
    }

    return type_chart.get((move_type, defender_type), 1)

def battle_turn(player_pokemon, opponent_pokemon):
    
    first, second = (player_pokemon, opponent_pokemon) if player_pokemon.speed >= opponent_pokemon.speed else (opponent_pokemon, player_pokemon)
    
    
    print(f"{first.name} choisit une attaque !")
    print("Choisissez une attaque :")
    for i, move in enumerate(first.moves):
        print(f"{i+1}. {move.name} (PP: {first.pp[move.name]})")

    
    while True:
        try:
            move_choice = int(input()) - 1  
            if move_choice < 0 or move_choice >= len(first.moves):
                print("Numéro d'attaque invalide. Essayez à nouveau.")
                continue  
            if first.pp[first.moves[move_choice].name] <= 0:
                print(f"{first.name} n'a plus de PP pour {first.moves[move_choice].name}!")
                continue  
            break  
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    player_move = first.get_move(move_choice)

    damage = calculate_damage(first, second, player_move)
    second.take_damage(damage)
    first.pp[player_move.name] -= 1
    print(f"{first.name} attaque {second.name} avec {player_move.name} pour {damage} dégâts!")

    opponent_move = random.choice(second.moves)
    damage = calculate_damage(second, first, opponent_move)
    first.take_damage(damage)
    second.pp[opponent_move.name] -= 1
    print(f"{second.name} attaque {first.name} avec {opponent_move.name} pour {damage} dégâts!")
