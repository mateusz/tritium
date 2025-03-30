from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Optional
from data_model.resource.resource import Resource

class EquipmentType(Enum):
    # Base Equipment
    DERRICK = auto()
    SELF_DESTRUCT_MECHANISM = auto()
    MASS_TRANSCIEVER = auto()
    AUTO_OPERATIONS_COMPUTER = auto()
    
    # Ship Equipment
    AUTO_CARGO_COMPUTER = auto()
    DRONE_FLEET_CONTROL_COMPUTER = auto()
    IOS_BATTLE_DRONE = auto()
    STAR_DRONE = auto()
    HYPERSPACE = auto()  # Hyperlight
    
    # Chassis
    SHUTTLE_CHASSIS = auto()
    IOS_CHASSIS = auto()
    SCG_CHASSIS = auto()
    
    # Drive Units
    SHUTTLE_DRIVE = auto()
    IOS_DRIVE = auto()
    SCG_DRIVE = auto()
    
    # Pods
    RESOURCE_POD = auto()
    TOOL_POD = auto()
    CRYO_POD = auto()
    PRISON_POD = auto()
    
    # Tools (installable on ToolPod)
    GRAPPLE = auto()
    INSTALLATION_REPAIR_EQUIPMENT = auto()  # Bandaid
    ASTEROID_MINING_ATTACHMENT = auto()
    RESOURCE_FACTORY_FRAME = auto()
    ORBITAL_FACTORY_FRAME = auto()
    COMMUNICATIONS_ADAPTER = auto()  # COMMSPOD
    PREJUDICE_TORPEDO_LAUNCHER = auto()
    PULSE_BLAST_LASER = auto()
    SONIC_BLASTER = auto()
    COMPLETE_ARTIFACT = auto()

@dataclass
class Equipment:
    """
    Base class for all equipment. All equipment can be built and stored in storage.
    """
    type: EquipmentType
    costs: Optional[Dict[Resource, int]] = None 