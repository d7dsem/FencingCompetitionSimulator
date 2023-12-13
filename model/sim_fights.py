from ctypes.wintypes import DOUBLE
import random
from prettytable import PrettyTable
from typing import Callable, Tuple

from .types import Fighter, Score, ClashResult, StatDict, HitsStat, FightsStat

from .sim_clash import emul_clash
from .scoring import ClashResultsPoints,hema_rule_set_v1

from utility.colorization import *



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

def test_fight_verbose():
    CF1=background_color(218, 22, 224) + foreground_color(10, 10, 10)
    CF2=background_color(5, 222, 255) + foreground_color(10, 10, 10)
    fighter1 = Fighter(id=f"{CF1}Sheep{COLOR_RESET}",
                       hit_chance=0.5, evade_chance=0.5,
                       fights=FightsStat(0,0,0),
                       hits=HitsStat(0,0,0), points=0  )
    
    fighter2 = Fighter(id=f"{CF2}Dear{COLOR_RESET}",
                       hit_chance=0.5, evade_chance=0.5,
                       fights=FightsStat(0,0,0),
                       hits=HitsStat(0,0,0), points=0 )

    print(fighter1)
    print(fighter2)
    print()
    
   
    scoring_core = ClashResultsPoints(clear_hit_value=3, double_hit_value=1, afterblow_coast=2)
    
    for i in range(0, 1, 1):
        print(f"{colorize(i+1):2} ", end = " ")
        emul_fight(f1=fighter1, f2=fighter2, scoring_core=scoring_core, win_score=10, rule_set=hema_rule_set_v1, verbose=True)    
        print()

def gen_fighter(hit_chance:float)->Fighter:
    pass

def sim_group(n: int=4)->None:
    matrix = [['' for _ in range(n)] for _ in range(n)]
    
    hit_chance_range=(0.45, 0.86)
    evade_chance_range=(0.35, 0.75)
    
    fighters = [Fighter.generate_fighter(hit_chance_range, evade_chance_range) for _ in range(n)]
    
    for i, f in enumerate(fighters, start=1):
        print(f"{i:2} {COLOR_OK}{f.id}{COLOR_RESET}\t{f}")
    print()
    
    
    table = PrettyTable()
    # Define column headers
    column_headers = ['Col1', 'Col2', 'Col3', 'Col4'] 
    table.field_names = ['----'] + column_headers

    # Define row headers
    row_headers = ['Row1', 'Row2', 'Row3', 'Row4']
    
    # Add rows to the table with row headers
    for header, row in zip(row_headers, matrix):
        table.add_row([header] + row)

    # Visualize the table
    print(table)