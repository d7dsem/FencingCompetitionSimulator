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
        print(f"{f1.id} hit {f2.id}| AB EMUL:", end=indent)
    ab2 = roll(f2.hit_chance)
    if ab2:        
        if verbose:
            print(f"{indent}{colorize(f2.id)} do AB hit |", end=indent)
        evade1 = roll(f1.evade_chance)
        if evade1:
            if verbose:
                print(f"{indent}{colorize(f1.id)} evade AB hit |", end=indent)
            return (ClashResult.CLEAR, ClashResult.MISSED, True)
        else:
            if verbose:
                print(f"{indent}{colorize(f1.id)} smack AB hit |", end=indent)
            return (ClashResult.CLEAR, ClashResult.AFTERBLOW, True)
    else:
        if verbose:
            print(f"{colorize(f2.id)} smack hit (w/o AB) |", end=indent)
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
        0:0 - обопільна "бабуйня" - виключаються з розгляду

    :param f1: Перший боєць.
    :param f2: Другий боєць.
    :param scoring: Базові значення для оцінок дій.
    :return: Пара очок, отриманих кожним бійцем.
    """
    
    if verbose:                    
        print(f"CLASH EMULATION: f1={f1.id} f2={f2.id}")
            
    r1 = ClashResult.MISSED
    r2 = ClashResult.MISSED
    isDone = False
    while not isDone:
        hit1 = roll(f1.hit_chance) and roll(f2.evade_chance)
        hit2 = roll(f2.hit_chance) and roll(f1.evade_chance)
        if hit1 and hit2:
            if verbose:
                print(f"DOUBLE |", end=indent)
            r1,r2,isDone = ClashResult.DOUBLE, ClashResult.DOUBLE, True
        else:
            if hit1:                        
                r1,r2,isDone = emul_after_blow(f1,f2,verbose)
            else:                    
                r2,r1,isDone = emul_after_blow(f2,f1,verbose)  
        
        if verbose:
            print(f"CLASH RES: ", end="")
            if isDone:
                # print(f"{f1.id} {colorize(r1)}:{colorize(r2)} {f2.id}")
                print(f"{colorize(r1)}:{colorize(r2)} |")
            else:
                print(f"BUBOOYNYA (0:0)")
                
    return (r1,r2)



