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
    
    @staticmethod
    def get_equipment(equipment_type: EquipmentType):
        """
        Return a specific equipment instance based on its type.
        This factory method creates and returns the appropriate equipment subclass.
        """
        # Base Equipment
        if equipment_type == EquipmentType.DERRICK:
            from data_model.equipment.base_equipment.derrick import Derrick
            return Derrick()
        elif equipment_type == EquipmentType.SELF_DESTRUCT_MECHANISM:
            from data_model.equipment.base_equipment.self_destruct_mechanism import SelfDestructMechanism
            return SelfDestructMechanism()
        elif equipment_type == EquipmentType.MASS_TRANSCIEVER:
            from data_model.equipment.base_equipment.mass_transciever import MassTransciever
            return MassTransciever()
        elif equipment_type == EquipmentType.AUTO_OPERATIONS_COMPUTER:
            from data_model.equipment.base_equipment.auto_operations_computer import AutoOperationsComputer
            return AutoOperationsComputer()
        elif equipment_type == EquipmentType.FUZ_LASER:
            from data_model.equipment.base_equipment.fuz_laser import FuzLaser
            return FuzLaser()
            
        # Ship Equipment
        elif equipment_type == EquipmentType.AUTO_CARGO_COMPUTER:
            from data_model.equipment.ship_equipment.auto_cargo_computer import AutoCargoComputer
            return AutoCargoComputer()
        elif equipment_type == EquipmentType.DRONE_FLEET_CONTROL_COMPUTER:
            from data_model.equipment.ship_equipment.drone_fleet_control_computer import DroneFleetControlComputer
            return DroneFleetControlComputer()
        elif equipment_type == EquipmentType.IOS_BATTLE_DRONE:
            from data_model.equipment.ship_equipment.ios_battle_drone import IOSBattleDrone
            return IOSBattleDrone()
        elif equipment_type == EquipmentType.STAR_DRONE:
            from data_model.equipment.ship_equipment.star_drone import StarDrone
            return StarDrone()
        elif equipment_type == EquipmentType.HYPERSPACE:
            from data_model.equipment.ship_equipment.hyperspace import Hyperspace
            return Hyperspace()
            
        # Chassis
        elif equipment_type == EquipmentType.SHUTTLE_CHASSIS:
            from data_model.equipment.ship_equipment.chassis.shuttle_chassis import ShuttleChassis
            return ShuttleChassis()
        elif equipment_type == EquipmentType.IOS_CHASSIS:
            from data_model.equipment.ship_equipment.chassis.ios_chassis import IOSChassis
            return IOSChassis()
        elif equipment_type == EquipmentType.SCG_CHASSIS:
            from data_model.equipment.ship_equipment.chassis.scg_chassis import SCGChassis
            return SCGChassis()
            
        # Drive Units
        elif equipment_type == EquipmentType.SHUTTLE_DRIVE:
            from data_model.equipment.ship_equipment.drive_unit.shuttle_drive import ShuttleDrive
            return ShuttleDrive()
        elif equipment_type == EquipmentType.IOS_DRIVE:
            from data_model.equipment.ship_equipment.drive_unit.ios_drive import IOSDrive
            return IOSDrive()
        elif equipment_type == EquipmentType.SCG_DRIVE:
            from data_model.equipment.ship_equipment.drive_unit.scg_drive import SCGDrive
            return SCGDrive()
            
        # Pods
        elif equipment_type == EquipmentType.RESOURCE_POD:
            from data_model.equipment.ship_equipment.pod.resource_pod import ResourcePod
            return ResourcePod()
        elif equipment_type == EquipmentType.TOOL_POD:
            from data_model.equipment.ship_equipment.pod.tool_pod import ToolPod
            return ToolPod()
        elif equipment_type == EquipmentType.CRYO_POD:
            from data_model.equipment.ship_equipment.pod.cryo_pod import CryoPod
            return CryoPod()
        elif equipment_type == EquipmentType.PRISON_POD:
            from data_model.equipment.ship_equipment.pod.prison_pod import PrisonPod
            return PrisonPod()
            
        # Tools
        elif equipment_type == EquipmentType.GRAPPLE:
            from data_model.equipment.ship_equipment.tool.grapple import Grapple
            return Grapple()
        elif equipment_type == EquipmentType.INSTALLATION_REPAIR_EQUIPMENT:
            from data_model.equipment.ship_equipment.tool.installation_repair_equipment import InstallationRepairEquipment
            return InstallationRepairEquipment()
        elif equipment_type == EquipmentType.ASTEROID_MINING_ATTACHMENT:
            from data_model.equipment.ship_equipment.tool.asteroid_mining_attachment import AsteroidMiningAttachment
            return AsteroidMiningAttachment()
        elif equipment_type == EquipmentType.RESOURCE_FACTORY_FRAME:
            from data_model.equipment.ship_equipment.tool.resource_factory_frame import ResourceFactoryFrame
            return ResourceFactoryFrame()
        elif equipment_type == EquipmentType.ORBITAL_FACTORY_FRAME:
            from data_model.equipment.ship_equipment.tool.orbital_factory_frame import OrbitalFactoryFrame
            return OrbitalFactoryFrame()
        elif equipment_type == EquipmentType.COMMUNICATIONS_ADAPTER:
            from data_model.equipment.ship_equipment.tool.communications_adapter import CommunicationsAdapter
            return CommunicationsAdapter()
        elif equipment_type == EquipmentType.PREJUDICE_TORPEDO_LAUNCHER:
            from data_model.equipment.ship_equipment.tool.prejudice_torpedo_launcher import PrejudiceTorpedoLauncher
            return PrejudiceTorpedoLauncher()
        elif equipment_type == EquipmentType.PULSE_BLAST_LASER:
            from data_model.equipment.ship_equipment.tool.pulse_blast_laser import PulseBlastLaser
            return PulseBlastLaser()
        elif equipment_type == EquipmentType.SONIC_BLASTER:
            from data_model.equipment.ship_equipment.tool.sonic_blaster import SonicBlaster
            return SonicBlaster()
        elif equipment_type == EquipmentType.COMPLETE_ARTIFACT:
            from data_model.equipment.ship_equipment.tool.complete_artifact import CompleteArtifact
            return CompleteArtifact()
        
        raise ValueError(f"Equipment type {equipment_type} not found")
    
    def get_research_technician_days(self) -> int:
        """
        Calculate the number of technician-days required to research this equipment.
        Scales proportionally with rank and the number of rare elements required.
        
        The base value is 700 technician-days for the simplest equipment.
        """
        # Base research time
        base_days = 700
        
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