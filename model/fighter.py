class Fighter:
    def __init__(self, fighter_id: str, hit_chance: float, evade_chance: float):
        """
        Ініціалізація фехтувальника з ID, шансами нанесення удару та уникнення удару.

        :param fighter_id: Унікальний ідентифікатор бійця.
        :param hit_chance: Ймовірність нанесення удару (від 0 до 1).
        :param evade_chance: Ймовірність уникнути удару (від 0 до 1).
        """
        self.id = fighter_id
        self.hit_chance = hit_chance
        self.evade_chance = evade_chance

    def __str__(self):
        return f"Fighter(ID: {self.id}, Hit Chance: {self.hit_chance}, Evade Chance: {self.evade_chance})"

