import random
from typing import Tuple

from .types import Fighter,ClashResult
from utility.colorization import colorize




indent = "  "

def roll(chance: float) -> bool:
    return random.random() > chance

def emul_after_blow(f1: Fighter, f2: Fighter, verbose: bool)-> Tuple[ClashResult, ClashResult, bool]:
    """
    Емуляція спроби афтерблоу другим бійцем після отриманого удару.
    Можливі результати:
      3:0 - перший боєць уник афтерблоу
      3:2 - другий боєць наніс афтерблоу
    """
    if verbose:
        print(f"{f1.id} HIT {f2.id}|", end=indent)
    ab2 = roll(f2.hit_chance)
    if ab2:        
        if verbose:
            print(f"{indent}{colorize(f2.id)} AB HIT |", end=indent)
        evade1 = roll(f1.evade_chance)
        if evade1:
            if verbose:
                print(f"{indent}{colorize(f1.id)} EVADE |", end=indent)
            return (ClashResult.CLEAR, ClashResult.MISSED, True)
        else:
            if verbose:
                print(f"{indent}{colorize(f1.id)} GET IT |", end=indent)
            return (ClashResult.CLEAR, ClashResult.AFTERBLOW, True)
    else:
        return (ClashResult.CLEAR, ClashResult.MISSED, True)

def emul_clash(f1: Fighter, f2: Fighter, verbose: bool) -> Tuple[ClashResult, ClashResult]:
    """
    Імітація сходу між двома бійцями.
    Трактування результатів:
        1:1 - обоюдка
        3:0 - перший наніс чистий удар
        0:3 - другий наніс чистий удар
        3:2 - перший наніс удар отримав афтерблоу
        2:3 - другий наніс удар отримав афтерблоу
        0:0 - обоюдна "бабуйня" - виключаються з розгляду

    :param f1: Перший боєць.
    :param f2: Другий боєць.
    :param scoring: Базові значення для оцінок дій.
    :return: Пара очок, отриманих кожним бійцем.
    """
    s1 = ClashResult.MISSED
    s2 = ClashResult.MISSED
    isDone = False
    while not isDone:        
        if roll(.5) :
            hit1 = roll(f1.hit_chance) and roll(f2.evade_chance)
            hit2 = roll(f2.hit_chance) and roll(f1.evade_chance)
            if hit1 and hit2:
                if verbose:
                    print(f"DOUBLE |", end=indent)
                s1,s2,isDone = ClashResult.DOUBLE, ClashResult.DOUBLE, True
            else:
                if hit1:                        
                    s1,s2,isDone = emul_after_blow(f1,f2,verbose)
                else:                    
                    s2,s1,isDone = emul_after_blow(f2,f1,verbose)  
            
            if verbose:
                print(f"CLASH RES - ", end="")
                if isDone:
                    print(f"{colorize(s1)}:{colorize(s2)}")
                else:
                    print(f"BUBOOYNYA (0:0)")
                
    return (s1,s2)



