#workflows folder includes scripts that can be run from command line

#This is only used to create a sublcass JSON 

from LVLUP.core.subclass import Subclass, Level, Upgrade, Feat, ProfOptions

import numpy as np

import json
from jsonic import serialize, deserialize

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

    #Available spells  
    SC.AS0 = ["mage hand","minor illusion","frostbite",
              "poison spray", "viscious Mockery (H)",
              "toll the dead", "spare the dying (H)",
              "light","guidance","decompose","encode thoughts (H)",
              "fire bolt"]
    SC.AS1 = ["charm person (H)","command (H)",
              "protection from good and evil", "burning hands",
              "fog","hex","shield","speak with animals",
              "Tasha's hideous laughter", "witch bolt","Sleep (H)",
              "Stare of the Witch (H*)","magic siphon (C)*"]
    


    #Dont forget to add spell list
    