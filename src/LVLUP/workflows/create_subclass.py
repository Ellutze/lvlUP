#workflows folder includes scripts that can be run from command line

#This is only used to create a sublcass JSON 

from LVLUP.core.subclass import Subclass, Level, Upgrade, Feat

from core.other import NPC

from core.PC import Action, Passive

import numpy as np

import json
from jsonic import serialize, deserialize

def create_subclass():


    #LVL 1

    SC = Subclass(name="Bookworm")

    #LVL1
    SC.levels[0].append = Upgrade(
        SS = np.asarray([5,0,0,0,0,0,0,0,0]),
        #number of profficiencies to select
        newCantrips = 3,
        newSpells = 2,
        selectProfs = 3,
        #...select from list
        profOptions = [ "investigation","nature","AH","insight",
                       "medicine","perception","survival"],
        ProfGiven = ["STint","STwis","light"]
        )
    
    #Each levels[x] holds upgrades for that level, not the total
    
    SC.levels[1].append = Upgrade(
        new_spells = 1,
        SS = np.asarray([1,0,0,0,0,0,0,0,0]),
        items = [NPC(description="Witches familiar sticks with the Witch, " \
        "   it is always around, almost magically. " \
        "This is not the “find familiar” spell - Witch familiar is an actual animal. " \
        "These familiars are smarter than their animal counterparts, and at some point stop aginig (players choice). " \
        "It only ages while the Witch allows. These familiars can die, but they are smart enough to avoid active combat.")]
        )
    
    #LVL3
    SC.levels[2].append = Upgrade(
        new_spells = 1,
        SS = np.asarray([2,1,0,0,0,0,0,0,0]),
        )
    
    #Default units feet!! (TODO note down somewhere)
    SC.levels[3].append = Upgrade(
        new_spells = 1,
        actions = [Action(name="borrowing",text="Witch can invade consciousness of another being, " \
        "seeing through their eyes and commanding their actions - " \
        "It is traditional that Witch thanks the target later for their service (i.e. by providing food). " \
        "To command a beast or animal to do something that would be against their nature will " \
        "require deception/persuasion checks resisted by target intelligence saving throw. " \
        "Takes bonus action in combat to cast, but can use actions of the target on their turn." \
        "Witch falls seemingly unconscious when cast. Takes action and bonus action in control of beast to return back"
        ,action_type = "a_ba",range=3000)],
        SS = np.asarray([0,1,0,0,0,0,0,0,0]),
        )
    
    SC.levels[4].append = Upgrade(
        SS = np.asarray([0,1,3,0,0,0,0,0,0]),
        new_spells = 1,
        actions = [Action(name="Your pain, my pain!",text="Once per short rest a Witch can take damage that would " \
            "otherwise be dealt to another within 10ft of her (this cannot be used if it would down the Witch). Bookworm can " \
            "also do the reverse to a willing player/creature (her damage received by another)vThis can be done to heal " \
            "people out of combat (needs to be pain-related injuries). The healing trades (lvl/2)*d6 damage "
            "(round to nearest integer mathematically)", RR = "short rest", action_type = "r")],
        passives = [Passive(name="Borrowing extension.",text="Bookworm (BW) learns about a type of entity (select from: elemental," \
        " fey, fiend, giant, ooze, dragon, construct, aberration). Basic members of this group (non-boses, non-unique monsters) " \
        "will be subject to BWs borrowing ability (similar to EMP for humanoids above). The Witch also gets a very good " \
        "understanding about that type of creature (resistances, hit-points, habitats, vulnerabilities, ACs… ).")]
    
        )

    SC.levels[5].append = Upgrade(
        SS = np.asarray([0,0,1,0,0,0,0,0,0]),
        actions = [Action(name="TheHotPoker",text="Attacks with improvised weapons can now be executed as bonus action.",action_type = "a_ba")]
        )
    
    SC.levels[6].append = Upgrade(
        SS = np.asarray([0,0,1,1,0,0,0,0,0]),
        )
    
    SC.levels[7].append = Upgrade(
        SS = np.asarray([0,0,0,2,0,0,0,0,0]),
        )
    
    SC.levels[8].append = Upgrade(
        SS = np.asarray([0,0,0,2,1,0,0,0,0]),
        )

    SC.levels[9].append = Upgrade(
        SS = np.asarray([2,0,0,0,2,0,0,0,0]),
        )
    SC.levels[10].append = Upgrade(
        SS = np.asarray([0,0,0,0,1,1,0,0,0]),
        )
    SC.levels[11].append = Upgrade(
        SS = np.asarray([0,0,0,0,0,0,0,0,0]),
        )
    SC.levels[12].append = Upgrade(
        SS = np.asarray([0,0,0,0,0,0,1,0,0]),
        )
    SC.levels[13].append = Upgrade(
        SS = np.asarray([0,0,0,0,0,0,0,0,0]),
        )
    SC.levels[14].append = Upgrade(
        SS = np.asarray([0,0,0,0,0,0,0,1,0]),
        )
    SC.levels[15].append = Upgrade(
        SS = np.asarray([0,0,0,0,0,0,0,0,0]),
        )
    SC.levels[16].append = Upgrade(
        SS = np.asarray([0,0,0,0,0,0,0,0,1]),
        )
    
    SC.levels[17].append = Upgrade(
        SS = np.asarray([0,0,0,0,1,0,0,0,0]),
        )
    
    SC.levels[18].append = Upgrade(
        SS = np.asarray([0,0,0,0,0,2,0,0,0]),
        )
    
    SC.levels[19].append = Upgrade(
        SS = np.asarray([0,0,0,0,0,0,2,0,0]),
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
    