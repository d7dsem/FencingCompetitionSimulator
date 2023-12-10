from utility.colorization import *
from model.scoring import ScoringValues
from model.fighter import Fighter
from model.sim_clash import *


CF1=background_color(218, 22, 224)
CF2=background_color(5, 222, 255)


enable_virtual_terminal_processing(True)

def greeting():
    print(colorize("HELLO STRANGER!"))
    
if __name__ == "__main__":
    greeting()
    
    scoring_system = ScoringValues(win_score=10,clear_hit_value=3, double_hit_value=1, afterblow_coast=2)

    print(scoring_system)
    
    fighter1 = Fighter(f"{CF1}Sheep{COLOR_RESET}", 0.5, 0.5)
    fighter2 = Fighter(f"{CF2}Bear {COLOR_RESET}",0.5, 0.5)

    print(fighter1)
    print(fighter2)
    print()
    
    # print(colorize("Emulate one clash:"))
    # rv = emul_clash(fighter1,fighter2,scoring_system)
    # print()
    
    print(colorize("Emulate fight:"))
    rv = emul_fight(fighter1,fighter2,scoring_system)
    print()
    
