

from pydantic import BaseModel, Field, ConfigDict, ValidationError, SerializeAsAny
import numpy as np
from typing import List, Optional, Tuple, Union, Annotated, Any
from datetime import date, time, timedelta

from LVLUP.core.subclass import ProfUP, Upgrade

class Specie(BaseModel):

    #Human is default as it is simplest

    # s = small, m = medium, l = large, sm = small/medium
    size: str = Field(default="sm")
    speed: int = Field(default=30)
    name: str = Field(default="human")
    #order ==> str, dex, cons, wis, int, cha
    selectionAbility: list = Field(default= [1,1,1,1,1,1])
    upgrades: list[Upgrade] = Field(default=[])
    

    #TODO languages


class Item(BaseModel):

    name: str = Field(default="Broom")

    #TODO