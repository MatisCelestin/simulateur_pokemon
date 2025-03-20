# move.py
class Move:
    def __init__(self, name, type_, power, accuracy, category, pp):
        self.name = name
        self.type = type_  # "Fire", "Water", etc.
        self.power = power
        self.accuracy = accuracy
        self.category = category  # "Physical" or "Special"
        self.pp = pp
