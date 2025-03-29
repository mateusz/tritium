from dataclasses import dataclass
from abc import ABC
from typing import Optional

from data_model.base.base import Base
from data_model.rank.rank import Rank
from data_model.vehicle.vehicle import Vehicle
from data_model.equipment.ship_equipment.pod.cryo_pod import CryoPod
@dataclass
class Personnel(ABC):
    """Abstract base for all personnel"""
    base: Optional[Base] = None
    rank: Optional[Rank] = None
    piloting: Optional[Vehicle] = None 
    cryo_pod: Optional[CryoPod] = None