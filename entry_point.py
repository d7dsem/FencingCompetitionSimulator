from utility.colorization import *

from model.sim_fights import emul_fight, random_fight, sim_group




enable_virtual_terminal_processing(True)

def greeting():
    print(colorize("<< HELLO STRANGER! >>"))
    print()
    
def bye_bye():
    print(colorize("<< THATS ALL! >>"))
    print()

if __name__ == "__main__":
    greeting()
    
    random_fight(verbose=False)
    
    sim_group()
    
    bye_bye()
    
