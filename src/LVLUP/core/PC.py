#PC contains player character objects 

from pydantic import BaseModel, Field, ConfigDict, ValidationError, SerializeAsAny
import numpy as np
from typing import List, Optional, Tuple, Union, Annotated, Any
from datetime import date, time, timedelta



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

class Profs(BaseModel):
    
    #Boolean only here

    #Weapons
    battleaxe: bool = Field(default=False)
    dagger: bool = Field(default=False)
    dart: bool = Field(default=False)
    flail: bool = Field(default=False)
    glaive: bool = Field(default=False)
    greatsword: bool = Field(default=False)
    halberd: bool = Field(default=False)
    #one handed
    crossbow_OH: bool = Field(default=False)
    #two handed
    crossbow_TH: bool = Field(default=False)
    shortsword: bool = Field(default=False)
    shortbow: bool = Field(default=False)
    longbow: bool = Field(default=False)
    imporov_weapon: bool = Field(default=False)
    javelin: bool = Field(default=False)
    mace: bool = Field(default=False)
    maul: bool = Field(default=False)
    morningstar: bool = Field(default=False)
    pistol: bool = Field(default=False)
    quarterstaff: bool = Field(default=False)
    rapier: bool = Field(default=False)
    scimitar: bool = Field(default=False)
    shield: bool = Field(default=False)
    spear: bool = Field(default=False)
    unarmed: bool = Field(default=False)
    


    #Instruments
    #TODO 

    #Languages 
    #TODO

    #Armour
    heavy: bool = Field(default=False)
    medium: bool = Field(default=False)
    light: bool = Field(default=False)

    #Saving throws
    STwis: bool = Field(default=False)
    STcha: bool = Field(default=False)
    STstr : bool = Field(default=False)
    STdex: bool = Field(default=False)
    STint : bool = Field(default=False)
    STcon: bool = Field(default=False)

    #skills int
    history: bool = Field(default=False)
    arcana: bool = Field(default=False)
    investigation: bool = Field(default=False)
    history: bool = Field(default=False)

    #wis skills
    medicine: bool = Field(default=False)
    survival: bool = Field(default=False)
    religion: bool = Field(default=False)
    insight : bool = Field(default=False)
    nature: bool = Field(default=False)
    perception: bool = Field(default=False)
    #animal handling
    AH: bool = Field(default=False)

    #str skills
    athletics: bool = Field(default=False)
    history: bool = Field(default=False)
    history: bool = Field(default=False)
    history: bool = Field(default=False)

    #dex skills
    #sleight of hand
    SOH: bool = Field(default=False)
    acrobatics: bool = Field(default=False)
    stealth: bool = Field(default=False)

    #cha skills
    persuation: bool = Field(default=False)
    deception: bool = Field(default=False)
    intimiddation: bool = Field(default=False)
    history: bool = Field(default=False)

    #kits
    #medkit
    MK: bool = Field(default=False)
    #thieves tools
    TT: bool = Field(default=False)
    #poisoners kit
    PK: bool = Field(default=False)


class PC(BaseModel):

    name: str = Field(default="Jon Doe")
    AS: Optional['AbilityScore'] = Field(default=AbilityScore())
    lvl: int = Field(default=1)
    specie: Specie = Field(default=Specie())

    #allow for multiclass by having list  subclasses
    #classes are implicit - subclasses is what matters
    subclass: Optional[list['Subclass']] = Field(default=[])

    hitDice: int = Field(default=0)
    prof_mod: int = Field(default=1)
    profs: 'Profs' = Field(default=Profs())

    resources: Res = Field(default=Res())

    items: list['Item'] = Field(default=0)

class Item(BaseModel):

    #Items are either equiped (default items rady at hand), or not ==> stashed in backpack - at least action to take out
    equiped: bool = Field(default=False)




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



