# pokemon.py
class Pokemon:
    def __init__(self, name, level, type_, hp, attack, defense, special_attack, special_defense, speed, moves):
        self.name = name
        self.level = level
        self.type = type_
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.moves = moves  
        self.pp = {move.name: move.pp for move in moves}  # Points de pouvoir
        self.status_conditions = []  

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def apply_status(self, status):
        if status not in self.status_conditions:
            self.status_conditions.append(status)

    def remove_status(self, status):
        if status in self.status_conditions:
            self.status_conditions.remove(status)

    def get_move(self, index):
        
        return self.moves[index]
