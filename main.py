# main.py
from move import Move
from pokemon import Pokemon
from battle import battle_turn

def create_pokemon():
    move1 = Move("Flamèche", "Fire", 40, 100, "Physical", 10)
    move2 = Move("Griffe", "Normal", 40, 100, "Physical", 10)
    move3 = Move("Hydrocanon", "Water", 110, 80, "Special", 5)
    move4 = Move("Morsure", "Dark", 60, 100, "Physical", 10)

    
    charizard = Pokemon("Charizard", 50, "Fire", 150, 100, 80, 100, 80, 100, [move1, move2, move3, move4])
    blastoise = Pokemon("Blastoise", 50, "Water", 160, 90, 100, 120, 100, 80, [move1, move2, move3, move4])
    
    return charizard, blastoise

def main():
    charizard, blastoise = create_pokemon()

    
    player_pokemon = charizard
    opponent_pokemon = blastoise

 
    while player_pokemon.is_alive() and opponent_pokemon.is_alive():
        print(f"\n{player_pokemon.name} (HP: {player_pokemon.hp}/{player_pokemon.max_hp}) contre {opponent_pokemon.name} (HP: {opponent_pokemon.hp}/{opponent_pokemon.max_hp})")
        battle_turn(player_pokemon, opponent_pokemon)

       
        if player_pokemon.is_alive():
            print("\nVoulez-vous changer de Pokémon ? (o/n)")
            choice = input()
            if choice.lower() == 'o':
                if player_pokemon == charizard:
                    player_pokemon = blastoise
                else:
                    player_pokemon = charizard
                print(f"Vous avez changé pour {player_pokemon.name}")

if __name__ == "__main__":
    main()
