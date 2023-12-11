from typing import Tuple, Callable

from utility.colorization import colorize
from .types import Fighter, HitsStat, ClashResult




class ClashResultsPoints:
    """
    Базові значеннями для опису можливих результатів одної сходки. Не для нарахування балів.
    
    clear_hit_value: бали за чисте ураження.
    double_hit_value: бали за обопільне ураження.
    afterblow_value: бали за успішний афтерблоу.
    """
    
    def __init__(self, clear_hit_value:int, afterblow_coast:int, double_hit_value:int):
        self.clear_hit_value = clear_hit_value
        self.double_hit_value = double_hit_value
        self.afterblow_value = afterblow_coast

    def __str__(self):
        return f"Clash Result Points (Clear Hit: {self.clear_hit_value} Afterblow: {self.afterblow_value}, Double Hit: {self.double_hit_value})"

    def ToPoints(self, r1: ClashResult, r2:ClashResult, eval: Callable[[ClashResult, ClashResult], Tuple[int, int]])->Tuple[int,int]:
        return eval(r1, r2)

def hema_rule_set_v1(r1:ClashResult,r2:ClashResult)->Tuple[int, int]:
    s1 = 0
    s2 = 0
    crp = ClashResultsPoints(3,2,1)
    if r1 == ClashResult.DOUBLE and r2 == ClashResult.DOUBLE:
        return 1,1
    if r1 == ClashResult.CLEAR:
        if r2 == ClashResult.AFTERBLOW:
            return 3,2
        else:
            return 3,0
    if r2 == ClashResult.CLEAR:
        if r1 == ClashResult.AFTERBLOW:
            return 2,3
        else:
            return 0,3
        
    return 0,0


