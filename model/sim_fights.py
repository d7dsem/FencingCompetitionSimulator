from ctypes.wintypes import DOUBLE
import random
from prettytable import PrettyTable
from typing import Callable, Tuple


from .sim_clash import emul_clash
from .scoring import ClashResultsPoints,hema_rule_set_v1
from .types import Fighter, Score, ClashResult, StatDict, HitsStat, FightsStat


from utility.colorization import *



def emul_fight(f1: Fighter, f2: Fighter, scoring_core: ClashResultsPoints, rule_set: Callable[[ClashResult, ClashResult], Tuple[int, int]],win_score: int, verbose: bool=False) -> Score:
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

def random_fight(verbose:bool=True)->Score:
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

    if verbose:
        print(fighter1)
        print(fighter2)
        print()
    
   
    scoring_core = ClashResultsPoints(clear_hit_value=3, double_hit_value=1, afterblow_coast=2)
    
    score = emul_fight(f1=fighter1, f2=fighter2, scoring_core=scoring_core, win_score=10, rule_set=hema_rule_set_v1, verbose=verbose)    
    if verbose:
        print()

    return score

def sim_group(n: int=4)->None:
    hit_chance_range=(0.45, 0.86)
    evade_chance_range=(0.35, 0.75)
    
    fighters = [Fighter.generate_fighter(hit_chance_range, evade_chance_range) for _ in range(n)]
    max_name_length = max(len(fighter.id) for fighter in fighters)
     
    for i, f in enumerate(fighters, start=1):
        print(f"{i:2} {colorize(f.id.ljust(max_name_length))}\t{f}")
    print()
    
    matrix = [['' for _ in range(n)] for _ in range(n)]
    win_score = 10
    scoring_core = ClashResultsPoints(clear_hit_value=3, double_hit_value=1, afterblow_coast=2)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 'Х'
                continue
            else:
                if j < i :
                    continue
                verbose = False
                # verbose = True
                score = emul_fight(fighters[i], fighters[j], scoring_core, hema_rule_set_v1, win_score, verbose)
                
                print(f"{colorize(fighters[i].id)} VS {colorize(fighters[j].id)}".ljust(max_name_length*2+6) + f"\t{score}")
                # print(f"{i},{j} <-- {colorize(score.s1)}     {j},{i} <-- {colorize(score.s2)}")
                
                matrix[i][j] = f"{colorize(score.s2)}"
                matrix[j][i] = f"{colorize(score.s1)}"
    
    print()
    
    for i, f in enumerate(fighters, start=1):
        print(f"{i:2} {colorize(f.id.ljust(max_name_length))}\t{f.fights}\t{f.hits}")
    print()
    
    show_group_result(fighters, max_name_length, matrix)

def show_group_result(fighters: list[Fighter], max_name_length: int, matrix:list[list[str]]):
    table = PrettyTable()
    
    # max_name_length = max(len(fighter.id) for fighter in fighters)
    
    # Define column headers
    column_headers = [fighter.id.ljust(max_name_length) for fighter in fighters] 
    table.field_names = ['----'] + column_headers
    # Define row headers
    row_headers = [fighter.id for fighter in fighters] 
    

            
    # Add rows to the table with row headers
    for header, row in zip(row_headers, matrix):
        table.add_row([header.ljust(max_name_length)] + row)
        # table.add_row([header] + row)

    # Visualize the table
    print(table)
    print()