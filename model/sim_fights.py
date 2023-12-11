from ctypes.wintypes import DOUBLE
import random
from typing import Callable, Tuple

from .types import Fighter, Score, ClashResult
from .sim_clash import emul_clash
from .scoring import ClashResultsPoints
from utility.colorization import colorize




def emul_fight(f1: Fighter, f2: Fighter, scoring_core: ClashResultsPoints, rule_set: Callable[[ClashResult, ClashResult], Tuple[int, int]],win_score: int, verbose: bool) -> Score:
    if verbose:
        print(f"{colorize('Emulate fight')} till {colorize(win_score)}\n  {scoring_core} ")
        print()

    cn = 1
    isAllDone = False
    while not isAllDone:
        if verbose:                    
            print(f"{colorize(cn):3} CLASH EMUL:")
        cn = cn + 1
        
        r1, r2 = emul_clash(f1,f2, verbose)
        clash_points_1, clash_points_2 = scoring_core.ToPoints(r1=r1,r2=r2,eval=rule_set)
        
        f1.points = f1.points + clash_points_1
        f1.hits.incrTotal()
        f1.hits.incrMissed()
        if clash_points_2==0:
            f1.hits.incrClear()
        
        f2.points = f2.points + clash_points_2
        f2.hits.incrTotal()
        f2.hits.incrMissed()
        if clash_points_1==0:
            f2.hits.incrClear()

        isAllDone =  (f1.points >= win_score or f2.points >= win_score)

        if verbose:
            print(f"SCORE:  ", end="  ")
            print(f"{colorize(f1.points)}:{colorize(f2.points)} |", end="   ")
            if isAllDone:
                print("FIN", end=" ")
            print()
    
    if verbose:
        print(f"Emulation completed. Niters={cn}.")
    

    if f1.points > f2.points:
        f1.fights.incrWin()
        f2.fights.incrLoose()
    elif f2.points > f1.points:
        f2.fights.incrWin()
        f1.fights.incrLoose()
    else:
        f1.fights.incrDraw()
        f2.fights.incrDraw()
    
    return Score(f1.points, f2.points)