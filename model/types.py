from enum import Enum
from typing import Dict
import uuid, random

from utility.colorization import colorize, background_color, foreground_color,COLOR_RESET

from utility.name_generation import gen_name



class Score:
    def __init__(self, s1,s2) -> None:
        self.s1=s1
        self.s2=s2
    def __str__(self) -> str:
        return f"SCORE: {colorize(self.s1)}:{colorize(self.s2)}"

class ClashResult(Enum):
    """
    Визначає базові оцінки можливих дій одного бійця
    """
    CLEAR = 3
    AFTERBLOW = 2
    DOUBLE = 1
    MISSED = 0
    
    def __str__(self):
        color = ""
        if self == ClashResult.CLEAR:
            color = background_color(7, 240, 69) + foreground_color(10, 10, 10)
        if self == ClashResult.AFTERBLOW:
            color = background_color(54, 138, 76) + foreground_color(10, 10, 10)
        if self == ClashResult.DOUBLE:
            color = background_color(222, 185, 22) + foreground_color(10, 10, 10)
        if self == ClashResult.MISSED:
            color = background_color(242, 97, 7) + foreground_color(10, 10, 10)
        return f'{color}{self.name}{COLOR_RESET}'

class FightsStat:
    def __init__(self, win:int, draw: int, loose:int):
        self.win =  win
        self.draw = draw
        self.loose = loose

    def incrWin(self, incrVal=1):
        self.win = self.win + incrVal
    def incrDraw(self, incrVal=1):
        self.draw = self.draw + incrVal
    def incrLoose(self, incrVal=1):
        self.loose = self.loose + incrVal    

    def __str__(self)->str:
        return f"win={self.win} draw={self.draw} loose={self.loose}"
    
class HitsStat:
    def __init__(self, deal:int, missed:int, clear:int):
        self.deal =  deal
        self.missed = missed
        self.clear = clear

    def incrClear(self, incrVal=1):
        self.clear = self.clear + incrVal    

    def incrTotal(self, incrVal=1):
        self.deal = self.deal + incrVal
        
    def incrMissed(self, incrVal=1):
        self.missed = self.missed + incrVal
        
    def __str__(self)->str:
        return f"deal={self.deal} clear={self.clear} missed={self.missed}"

StatDict = dict[str,HitsStat]

class Fighter:
    def __init__(self, id: str, hit_chance: float, evade_chance: float, hits: HitsStat, fights: FightsStat, points: int):
        """
        Ініціалізація фехтувальника з ID, шансами нанесення удару та уникнення удару.

        :param fighter_id: Унікальний ідентифікатор бійця.
        :param hit_chance: Ймовірність нанесення удару (від 0 до 1).
        :param evade_chance: Ймовірність уникнути удару (від 0 до 1).
        """
        self.id = id
        self.hit_chance = hit_chance
        self.evade_chance = evade_chance
        self.hits = hits
        self.fights = fights
        self.points = points

    def __str__(self)->str:
        return f"Fighter(ID: {self.id}, Hit Chance: {self.hit_chance}, Evade Chance: {self.evade_chance} Fights: {self.fights}, Hits: {self.hits}, Point:{self.points})"

    @staticmethod
    def generate_fighter(hit_chance_range, evade_chance_range, id=None):
        """
        Static method to generate a Fighter instance. 
        If 'id' is not provided, it generates a unique id.
        """
        # Validate the hit_chance_range and evade_chance_range
        if (hit_chance_range[0] < 0 or hit_chance_range[1] > 1 or 
            evade_chance_range[0] < 0 or evade_chance_range[1] > 1):
            raise ValueError("Hit and evade chances must be between 0 and 1")

        # Generate random hit_chance and evade_chance within the given ranges
        hit_chance = random.uniform(*hit_chance_range)
        evade_chance = random.uniform(*evade_chance_range)

        # Generate a unique id if not provided
        if id is None:
            id = str(uuid.uuid4())
            id = gen_name()

        # Initialize hits, fights, and points with default values
        hits = HitsStat(0,0,0)  
        fights = FightsStat(0,0,0)
        points = 0  # Default value

        # Create and return the Fighter instance
        return Fighter(id, hit_chance, evade_chance, hits, fights, points)