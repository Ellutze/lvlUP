#workflows folder includes scripts that can be run from command line

#This is only used to create a sublcass JSON 

from LVLUP.core.subclass import Subclass, Level, Upgrade, Feat, ProfOptions

import numpy as np

def create_subclass():


    #LVL 1

    SC = Subclass(name="Bookworm")

    
    SC.levels[0].append = Upgrade(
        SL = np.asarray([3,2,0,0,0,0,0,0,0,0]),
        SS = np.asarray([5,0,0,0,0,0,0,0,0]),
        profOptions = ProfOptions(number = 3, selection=[
        "investigation","nature","AH","insight","medicine",
        "perception","survival"]),
        ProfGiven = ["STint","STwis","light"]

        )
    
    #Dont forget to add spell list
    