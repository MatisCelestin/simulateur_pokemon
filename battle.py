import random

def calculate_damage(attacker, defender, move):
    """
    Calcule les dégâts infligés par un Pokémon (attacker) à un autre (defender)
    en utilisant un mouvement spécifique (move).
    """
    # Calcul des dégâts selon la formule officielle de Pokémon
    # Dégâts = (((2 * niveau / 5 + 2) * puissance * attaque / défense) / 50) + 2
    level = attacker.level
    power = move.power
    if move.category == "Physical":  # Attaque physique
        attack = attacker.attack
        defense = defender.defense
    elif move.category == "Special":  # Attaque spéciale
        attack = attacker.special_attack
        defense = defender.special_defense
    else:
        return 0  # Si le mouvement est de type autre, on retourne 0 (pas de dégâts)

    # Appliquer la formule des dégâts de Pokémon
    damage = (((2 * level / 5 + 2) * power * attack / defense) / 50) + 2

    # Prendre en compte les faiblesses et résistances des types
    effectiveness = type_effectiveness(move.type, defender.type)
    damage *= effectiveness

    return int(damage)

def type_effectiveness(move_type, defender_type):
    """
    Calcule l'efficacité d'un mouvement en fonction de la faiblesse/résistance du défenseur.
    """
    # Exemple simplifié d'efficacité des types (à améliorer pour couvrir tous les types)
    type_chart = {
        ("Fire", "Grass"): 2,  # Le feu est efficace contre l'herbe
        ("Water", "Fire"): 2,  # L'eau est efficace contre le feu
        ("Water", "Electric"): 0.5,  # L'eau est résistante contre l'électrique
        ("Electric", "Water"): 2,  # L'électricité est efficace contre l'eau
        ("Fire", "Water"): 0.5,  # Le feu est moins efficace contre l'eau
        ("Electric", "Ground"): 0,  # L'électricité ne fonctionne pas contre le sol
        # Ajoutez ici d'autres relations de types si nécessaire
    }

    return type_chart.get((move_type, defender_type), 1)  # 1 signifie efficacité normale (aucun effet)

def battle_turn(player_pokemon, opponent_pokemon):
    # Le Pokémon le plus rapide attaque en premier
    first, second = (player_pokemon, opponent_pokemon) if player_pokemon.speed >= opponent_pokemon.speed else (opponent_pokemon, player_pokemon)
    
    # Le joueur choisit une attaque
    print(f"{first.name} choisit une attaque !")
    print("Choisissez une attaque :")
    for i, move in enumerate(first.moves):
        print(f"{i+1}. {move.name} (PP: {first.pp[move.name]})")

    # Boucle pour valider la saisie du joueur
    while True:
        try:
            move_choice = int(input()) - 1  # Le joueur entre un numéro (1-4)
            if move_choice < 0 or move_choice >= len(first.moves):
                print("Numéro d'attaque invalide. Essayez à nouveau.")
                continue  # Redemander la saisie
            if first.pp[first.moves[move_choice].name] <= 0:
                print(f"{first.name} n'a plus de PP pour {first.moves[move_choice].name}!")
                continue  # Redemander la saisie si l'attaque a épuisé ses PP
            break  # Sortir de la boucle si la saisie est correcte
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    player_move = first.get_move(move_choice)

    # Attaque du joueur
    damage = calculate_damage(first, second, player_move)
    second.take_damage(damage)
    first.pp[player_move.name] -= 1
    print(f"{first.name} attaque {second.name} avec {player_move.name} pour {damage} dégâts!")

    # L'adversaire choisit une attaque aléatoire
    opponent_move = random.choice(second.moves)
    damage = calculate_damage(second, first, opponent_move)
    first.take_damage(damage)
    second.pp[opponent_move.name] -= 1
    print(f"{second.name} attaque {first.name} avec {opponent_move.name} pour {damage} dégâts!")
