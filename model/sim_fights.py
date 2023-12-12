from ctypes.wintypes import DOUBLE
import random
from typing import Callable, Tuple

from .types import Fighter, Score, ClashResult
from .sim_clash import emul_clash
from .scoring import ClashResultsPoints
from utility.colorization import colorize




def emul_fight(f1: Fighter, f2: Fighter, scoring_core: ClashResultsPoints, rule_set: Callable[[ClashResult, ClashResult], Tuple[int, int]],win_score: int, verbose: bool) -> Score:
    if verbose:
        print(f"{colorize('FIGHT EMULATION')} till {colorize(win_score)}\n    {scoring_core}")

    cn = 1
    isAllDone = False
    s1 = 0
    s2 = 0
    while not isAllDone:
        if verbose:                    
            print(f"{colorize(cn):3} ", end=" ")
        cn = cn + 1
        
        r1, r2 = emul_clash(f1,f2, verbose)
        
        clash_points_1, clash_points_2 = scoring_core.ToPoints(r1=r1,r2=r2,eval=rule_set)
        s1 =s1 + clash_points_1
        s2 =s2 + clash_points_2
        
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

        isAllDone =  (s1 >= win_score or s2 >= win_score)

        if verbose:
            print(f"[{Score(s1,s2)}]")
            
    
    res = Score(s1, s2)
    
    if verbose:
        print(f"{colorize('EMULATION COMPETED')}: count_clash={colorize(cn) }")
        print(f"[{res}]")
    

    if f1.points > f2.points:
        f1.fights.incrWin()
        f2.fights.incrLoose()
    elif f2.points > f1.points:
        f2.fights.incrWin()
        f1.fights.incrLoose()
    else:
        f1.fights.incrDraw()
        f2.fights.incrDraw()
    
    return res