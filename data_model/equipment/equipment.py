from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Optional
from data_model.resource.resource import Resource
from data_model.rank.researcher_rank import ResearcherRank
class EquipmentType(Enum):
    # Base Equipment
    DERRICK = auto()
    SELF_DESTRUCT_MECHANISM = auto()
    MASS_TRANSCIEVER = auto()
    AUTO_OPERATIONS_COMPUTER = auto()
    FUZ_LASER = auto()
    
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

class RequiredLocation(Enum):
    ANY_FACTORY = auto()
    ORBIT_ONLY = auto()

@dataclass
class Equipment:
    """
    Base class for all equipment. All equipment can be built and stored in storage.
    """
    type: EquipmentType
    costs: Optional[Dict[Resource, int]] = None 
    mass: Optional[int] = None
    required_rank: Optional[ResearcherRank] = None
    required_location: Optional[RequiredLocation] = None 
    

    
    def get_research_technician_days(self) -> int:
        """
        Calculate the number of technician-days required to research this equipment.
        Scales proportionally with rank and the number of rare elements required.
        
        The base value is 1400 technician-days for the simplest equipment.
        """
        # Base research time
        base_days = 1400
        
        # Rank multiplier based on ResearcherRank enum
        rank_multiplier = 1.0  # Default for no rank requirement
        if self.required_rank is not None:
            if self.required_rank == ResearcherRank.TECHNICIAN:
                rank_multiplier = 1.0
            elif self.required_rank == ResearcherRank.DOCTOR:
                rank_multiplier = 1.5
            elif self.required_rank == ResearcherRank.PROFESSOR:
                rank_multiplier = 2.0
        
        # Count rare elements in costs
        rare_elements_count = 0
        if self.costs is not None:
            # Consider these resources as rare
            rare_resources = [
                Resource.PALLADIUM, 
                Resource.PLATINUM, 
                Resource.SILVER, 
                Resource.GOLD, 
                Resource.DEUTERIUM
            ]
            
            for resource in self.costs:
                if resource in rare_resources:
                    rare_elements_count += 1
        
        # Rare elements multiplier (each rare element adds 0.2 to multiplier)
        rare_multiplier = 1 + (rare_elements_count * 0.2)
        
        # Calculate total technician-days
        total_days = int(base_days * rank_multiplier * rare_multiplier)
        
        return total_days 