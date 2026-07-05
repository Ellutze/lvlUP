#PC contains player character objects 

from pydantic import BaseModel, Field, ConfigDict, ValidationError, SerializeAsAny
import numpy as np
from typing import List, Optional, Tuple, Union, Annotated, Any, Literal
from datetime import date, time, timedelta
from other import Specie, Item, NPC, Prof



class FileMetadata(BaseModel):
    #the below might be housed in specialized class
    lastModified: Optional[str] = Field(default=None) #Automatically refresh on save - string for json parsing
    lastModifiedBy: Optional[str] = Field(default=None) #String name
    version: Optional[str] = Field(default= "0.0.0") #eg. - type is stirng now, for lack of better options

    #log
    editHistory: Optional[list['Edit']] = Field(default=None)


class Edit(BaseModel):

    ref: Optional[str] = Field(default=None)
    before: Optional[Any] = Field(default=None)
    after: Optional[Any] = Field(default=None)

class Res(BaseModel):

    #
    gold: float = Field(default=0)

    #spell slots (row 1 current, row 2max)
    SS: Annotated[np.ndarray, Field(default_factory=lambda: np.zeros((2, 9)))]
    #hit dice current
    curHD: int = Field(default=0)
    #max hit dice = char level, so no need for specific param

    #sorcery points
    sp: int = Field(default=0)
    #channeled divinity

    #lay on hands

    #

class Action(BaseModel):

    name: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)
    #a = action , ba = bonus action, a_ba is either action or bonus action, u = unique resource, r = reaction
    action_type: Optional[Literal["a", "ba", "a_ba","u","r"]] = Field(default=None)
    range: Optional[float] = Field(default=None)
    #Resource recovery
    RR: Optional[Literal["short rest","long rest"]] = Field(default=None)

class Passive(BaseModel):

    name: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)

class ExtraActions(BaseModel):

    #unique resource amount required
    ura = Optional[int] = Field(default=0)

class ExtraPassives(Passive):

    #Conditions under which this applies
    condition = Optional[str] = Field(default=None)


class Profs(BaseModel):
    
    #Boolean only here

    #Weapons
    battleaxe: Prof = Field(default=Prof(name="battleaxe"))
    dagger: Prof = Field(default=Prof(name="dagger"))
    dart: Prof = Field(default=Prof(name="dart"))
    flail: Prof = Field(default=Prof(name="flail"))
    glaive: Prof = Field(default=Prof(name="glaive"))
    greatsword: Prof = Field(default=Prof(name="greatsword"))
    halberd: Prof = Field(default=Prof(name="halberd"))

    # one handed
    crossbow_OH: Prof = Field(default=Prof(name="crossbow_OH"))

    # two handed
    crossbow_TH: Prof = Field(default=Prof(name="crossbow_TH"))

    shortsword: Prof = Field(default=Prof(name="shortsword"))
    shortbow: Prof = Field(default=Prof(name="shortbow"))
    longbow: Prof = Field(default=Prof(name="longbow"))
    imporov_weapon: Prof = Field(default=Prof(name="imporov_weapon"))
    javelin: Prof = Field(default=Prof(name="javelin"))
    mace: Prof = Field(default=Prof(name="mace"))
    maul: Prof = Field(default=Prof(name="maul"))
    morningstar: Prof = Field(default=Prof(name="morningstar"))
    pistol: Prof = Field(default=Prof(name="pistol"))
    quarterstaff: Prof = Field(default=Prof(name="quarterstaff"))
    rapier: Prof = Field(default=Prof(name="rapier"))
    scimitar: Prof = Field(default=Prof(name="scimitar"))
    shield: Prof = Field(default=Prof(name="shield"))
    spear: Prof = Field(default=Prof(name="spear"))
    unarmed: Prof = Field(default=Prof(name="unarmed"))

    # Instruments
    lute: Prof = Field(default=Prof(name="lute"))
    flute: Prof = Field(default=Prof(name="flute"))
    drum: Prof = Field(default=Prof(name="drum"))
    lyre: Prof = Field(default=Prof(name="lyre"))
    horn: Prof = Field(default=Prof(name="horn"))
    bagpipes: Prof = Field(default=Prof(name="bagpipes"))

    # Languages
    common: Prof = Field(default=Prof(name="common"))
    elvish: Prof = Field(default=Prof(name="elvish"))
    dwarvish: Prof = Field(default=Prof(name="dwarvish"))
    orc: Prof = Field(default=Prof(name="orc"))
    goblin: Prof = Field(default=Prof(name="goblin"))
    draconic: Prof = Field(default=Prof(name="draconic"))
    infernal: Prof = Field(default=Prof(name="infernal"))
    celestial: Prof = Field(default=Prof(name="celestial"))

    # Armour
    heavy: Prof = Field(default=Prof(name="heavy"))
    medium: Prof = Field(default=Prof(name="medium"))
    light: Prof = Field(default=Prof(name="light"))

    # Saving throws
    STwis: Prof = Field(default=Prof(name="STwis"))
    STcha: Prof = Field(default=Prof(name="STcha"))
    STstr: Prof = Field(default=Prof(name="STstr"))
    STdex: Prof = Field(default=Prof(name="STdex"))
    STint: Prof = Field(default=Prof(name="STint"))
    STcon: Prof = Field(default=Prof(name="STcon"))

    # skills int
    history: Prof = Field(default=Prof(name="history"))
    arcana: Prof = Field(default=Prof(name="arcana"))
    investigation: Prof = Field(default=Prof(name="investigation"))

    # wis skills
    medicine: Prof = Field(default=Prof(name="medicine"))
    survival: Prof = Field(default=Prof(name="survival"))
    religion: Prof = Field(default=Prof(name="religion"))
    insight: Prof = Field(default=Prof(name="insight"))
    nature: Prof = Field(default=Prof(name="nature"))
    perception: Prof = Field(default=Prof(name="perception"))

    # animal handling
    AH: Prof = Field(default=Prof(name="AH"))

    # str skills
    athletics: Prof = Field(default=Prof(name="athletics"))

    # dex skills
    # sleight of hand
    SOH: Prof = Field(default=Prof(name="SOH"))
    acrobatics: Prof = Field(default=Prof(name="acrobatics"))
    stealth: Prof = Field(default=Prof(name="stealth"))

    # cha skills
    persuation: Prof = Field(default=Prof(name="persuation"))
    deception: Prof = Field(default=Prof(name="deception"))
    intimiddation: Prof = Field(default=Prof(name="intimiddation"))

    # kits
    # medkit
    MK: Prof = Field(default=Prof(name="MK"))

    # thieves tools
    TT: Prof = Field(default=Prof(name="TT"))

    # poisoners kit
    PK: Prof = Field(default=Prof(name="PK"))


class PC(BaseModel):

    name: str = Field(default="Jon Doe")
    AS: Optional['AbilityScore'] = Field(default=AbilityScore())
    lvl: int = Field(default=1)
    specie: Specie = Field(default=Specie())
    #armour class
    AC: float = Field(default=10)

    XP: float = Field(default=0)

    #allow for multiclass by having list  subclasses
    #classes are implicit - subclasses is what matters
    subclass: Optional[list['Subclass']] = Field(default=[])

    hitDice: int = Field(default=0)
    prof_mod: int = Field(default=1)
    profs: 'Profs' = Field(default=Profs())

    resources: Res = Field(default=Res())

    actions: Res = Field(default=Action)
    passives: Res = Field(default=Passive)

    items: list['Item'] = Field(default=0)

    notes: str = Field(default="")
    followers: list[NPC] = Field(default_factory=list)






class Subclass(BaseModel):

    CLASS: Optional[str] = Field(default=None)
    #subclass name
    sc: Optional[str] = Field(default=None)
    lvl: int = Field(default=1)





class AbilityScore(BaseModel):

    STR: float = Field(default=10)
    DEX: float = Field(default=10)
    CON: float = Field(default=10)
    STR: float = Field(default=10)
    DEX: float = Field(default=10)
    CON: float = Field(default=10)

    #Permanent Ability scores are the default after effects wear off
    pSTR: float = Field(default=10)
    pDEX: float = Field(default=10)
    pCON: float = Field(default=10)
    pSTR: float = Field(default=10)
    pDEX: float = Field(default=10)
    pCON: float = Field(default=10)

    method: Optional[str] = Field(default=None)

class Effect(BaseModel):

    #expires after no. long rests and short rests
    expLR: int = Field(default=0)
    expSR: int = Field(default=1)



