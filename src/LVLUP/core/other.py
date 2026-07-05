

from pydantic import BaseModel, Field, ConfigDict, ValidationError, SerializeAsAny
import numpy as np
from typing import List, Optional, Tuple, Union, Annotated, Any
from datetime import date, time, timedelta
from PC import Action, Passive, AbilityScore

from LVLUP.core.subclass import ProfUP, Upgrade

class Specie(BaseModel):

    name: str = Field(default="Human")#
    #ability score bonuses
    ASB: Annotated[np.ndarray, Field(default_factory=lambda: np.asarra([1,1,1,1,1,1]))]
    passives: Passive = Field(default=[])
    actions: Action = Field(default=[])
    size: float = Field(default="5.5")
    speed: float = Field(default="30")
    languages: list = Field(default=["common"])

    

    #TODO languages


class Item(BaseModel):

    #Items are either equiped (default items rady at hand), or not ==> stashed in backpack - at least action to take out
    equiped: bool = Field(default=False)
    item_type: str = Field(default="")
    description: str = Field(default=None)

class NPC(BaseModel):

    AC: float = Field(default=0)
    AS: AbilityScore = Field(default=AbilityScore())
