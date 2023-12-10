import random
from typing import Tuple

from .fighter import Fighter
from .scoring import ScoringValues
from utility.colorization import colorize




verbose = True

indent = "  "

def roll(chance: float) -> bool:
    return random.random() > chance

def emul_fighter1_hit(f1: Fighter, f2: Fighter, scoring: ScoringValues)-> Tuple[int, int, bool]:
    evade2 = roll(f2.evade_chance)
    if evade2:
        if verbose:
            print(f"{indent}{colorize(f2.id)} EVADE |", end=indent)
        return (0,0,False)
    ab2 = roll(f2.hit_chance)
    if ab2:
        if verbose:
            print(f"{indent}{colorize(f2.id)} AB {colorize(f1.id)} |", end=indent)
        evade1 = roll(f1.evade_chance)
        if evade1:
            if verbose:
                print(f"{indent}{colorize(f1.id)} EVADE AB |", end=indent)
            return (scoring.clear_hit_value, 0, True)
        else:
            if verbose:
                print(f"{indent}{colorize(f1.id)} GET AB |", end=indent)
            return (scoring.double_hit_value, scoring.double_hit_value, True)
    else:        
        return (scoring.clear_hit_value, 0, True)
    

def emul_clash(f1: Fighter, f2: Fighter, scoring: ScoringValues) -> Tuple[int, int]:
    """
    Імітація сходу між двома бійцями.

    :param f1: Перший боєць.
    :param f2: Другий боєць.
    :param scoring: Система оцінювання.
    :return: Пара очок, отриманих кожним бійцем.
    """
    s1 = 0
    s2 = 0
    isDone = False
    while not isDone:        
        if roll(.5) :
            hit1 = roll(f1.hit_chance)
            if hit1:
                if verbose:
                    print(f"{colorize(f1.id)} HIT {colorize(f2.id)} |", end=indent)
                s1,s2,isDone = emul_fighter1_hit(f1,f2,scoring)
            else:
                if verbose:
                    print(f"{colorize(f2.id)} HIT {colorize(f1.id)} |", end=indent)
                s2,s1,isDone = emul_fighter1_hit(f2,f1,scoring)  
            if verbose:
                print(f"CLASH RES - ", end="")
                if isDone:
                    print(f"{colorize(s1)}:{colorize(s2)}")
                else:
                    print(f"BUBOOYNYA")
                
    return (s1,s2)

def emul_fight(f1: Fighter, f2: Fighter, scoring: ScoringValues) -> Tuple[int, int]:
    s2 = 0
    s1 = 0
    cn = 1
    while not (s2 >= scoring.win_score or s1 >= scoring.win_score):
        if verbose:                    
            print(f"{colorize(cn):3} CLASH EMUL:")
            cn = cn + 1
        t1, t2 = emul_clash(f1,f2,scoring)
        s1 = s1 + t1
        s2 = s2 + t2
        if verbose:
            print(f"SCORE - {colorize(s1)}:{colorize(s2)}")              
            print("")
    
    return (s1, s2)
        
    
