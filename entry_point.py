from utility.colorization import *

from model.scoring import ClashResultsPoints, hema_rule_set_v1
from model.types import Fighter, StatDict, HitsStat, FightsStat

from model.sim_fights import emul_fight


CF1=background_color(218, 22, 224) + foreground_color(10, 10, 10)
CF2=background_color(5, 222, 255) + foreground_color(10, 10, 10)


enable_virtual_terminal_processing(True)

def greeting():
    print(colorize("<< HELLO STRANGER! >>"))
    print()
    
def bye_bye():
    print(colorize("<< THATS ALL! >>"))
    print()
        
if __name__ == "__main__":
    greeting()
    
    # my_dict = StatDict({ "HEMA":HitStat(0,0,0), "HORT": HitStat(0,0,0) })
    
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
    
    # print(colorize("Emulate one clash:"))
    # rv = emul_clash(fighter1,fighter2,scoring_system)
    # print()
    
    
    # rv = emul_fight_frame(f1=fighter1,f2=fighter2,verbose=True)
    
    scoring_core = ClashResultsPoints(clear_hit_value=3, double_hit_value=1, afterblow_coast=2)
    
    emul_fight(f1=fighter1, f2=fighter2, scoring_core=scoring_core, win_score=10, rule_set=hema_rule_set_v1, verbose=True)    
    print()
    
    bye_bye()
    
