from coordinators.coordinator import Coordinator
from data_model.equipment.equipment import EquipmentType
from data_model.equipment.base_equipment.derrick import Derrick
from data_model.equipment.base_equipment.self_destruct_mechanism import SelfDestructMechanism
from data_model.equipment.base_equipment.mass_transciever import MassTransciever
from data_model.equipment.base_equipment.auto_operations_computer import AutoOperationsComputer
from data_model.equipment.base_equipment.fuz_laser import FuzLaser
from data_model.equipment.ship_equipment.auto_cargo_computer import AutoCargoComputer
from data_model.equipment.ship_equipment.drone_fleet_control_computer import DroneFleetControlComputer
from data_model.equipment.ship_equipment.ios_battle_drone import IOSBattleDrone
from data_model.equipment.ship_equipment.star_drone import StarDrone
from data_model.equipment.ship_equipment.hyperspace import Hyperspace
from data_model.equipment.ship_equipment.chassis.shuttle_chassis import ShuttleChassis
from data_model.equipment.ship_equipment.chassis.ios_chassis import IOSChassis
from data_model.equipment.ship_equipment.chassis.scg_chassis import SCGChassis
from data_model.equipment.ship_equipment.drive_unit.shuttle_drive import ShuttleDrive
from data_model.equipment.ship_equipment.drive_unit.ios_drive import IOSDrive
from data_model.equipment.ship_equipment.drive_unit.scg_drive import SCGDrive
from data_model.equipment.ship_equipment.pod.resource_pod import ResourcePod
from data_model.equipment.ship_equipment.pod.tool_pod import ToolPod
from data_model.equipment.ship_equipment.pod.cryo_pod import CryoPod
from data_model.equipment.ship_equipment.pod.prison_pod import PrisonPod
from data_model.equipment.ship_equipment.tool.grapple import Grapple
from data_model.equipment.ship_equipment.tool.installation_repair_equipment import InstallationRepairEquipment
from data_model.equipment.ship_equipment.tool.asteroid_mining_attachment import AsteroidMiningAttachment
from data_model.equipment.ship_equipment.tool.resource_factory_frame import ResourceFactoryFrame
from data_model.equipment.ship_equipment.tool.orbital_factory_frame import OrbitalFactoryFrame
from data_model.equipment.ship_equipment.tool.communications_adapter import CommunicationsAdapter
from data_model.equipment.ship_equipment.tool.prejudice_torpedo_launcher import PrejudiceTorpedoLauncher
from data_model.equipment.ship_equipment.tool.pulse_blast_laser import PulseBlastLaser
from data_model.equipment.ship_equipment.tool.sonic_blaster import SonicBlaster
from data_model.equipment.ship_equipment.tool.complete_artifact import CompleteArtifact

class EquipmentCoordinator(Coordinator):
    
    def get_equipment(self, equipment_type: EquipmentType):
        """
        Return a specific equipment instance based on its type.
        This factory method creates and returns the appropriate equipment subclass.
        """
        # Base Equipment
        if equipment_type == EquipmentType.DERRICK:
            return Derrick()
        elif equipment_type == EquipmentType.SELF_DESTRUCT_MECHANISM:
            return SelfDestructMechanism()
        elif equipment_type == EquipmentType.MASS_TRANSCIEVER:
            return MassTransciever()
        elif equipment_type == EquipmentType.AUTO_OPERATIONS_COMPUTER:
            return AutoOperationsComputer()
        elif equipment_type == EquipmentType.FUZ_LASER:
            return FuzLaser()
            
        # Ship Equipment
        elif equipment_type == EquipmentType.AUTO_CARGO_COMPUTER:
            return AutoCargoComputer()
        elif equipment_type == EquipmentType.DRONE_FLEET_CONTROL_COMPUTER:
            return DroneFleetControlComputer()
        elif equipment_type == EquipmentType.IOS_BATTLE_DRONE:
            return IOSBattleDrone()
        elif equipment_type == EquipmentType.STAR_DRONE:
            return StarDrone()
        elif equipment_type == EquipmentType.HYPERSPACE:
            return Hyperspace()
            
        # Chassis
        elif equipment_type == EquipmentType.SHUTTLE_CHASSIS:
            return ShuttleChassis()
        elif equipment_type == EquipmentType.IOS_CHASSIS:
            return IOSChassis()
        elif equipment_type == EquipmentType.SCG_CHASSIS:
            return SCGChassis()
            
        # Drive Units
        elif equipment_type == EquipmentType.SHUTTLE_DRIVE:
            return ShuttleDrive()
        elif equipment_type == EquipmentType.IOS_DRIVE:
            return IOSDrive()
        elif equipment_type == EquipmentType.SCG_DRIVE:
            return SCGDrive()
            
        # Pods
        elif equipment_type == EquipmentType.RESOURCE_POD:
            return ResourcePod()
        elif equipment_type == EquipmentType.TOOL_POD:
            return ToolPod()
        elif equipment_type == EquipmentType.CRYO_POD:
            return CryoPod()
        elif equipment_type == EquipmentType.PRISON_POD:
            return PrisonPod()
            
        # Tools
        elif equipment_type == EquipmentType.GRAPPLE:
            return Grapple()
        elif equipment_type == EquipmentType.INSTALLATION_REPAIR_EQUIPMENT:
            return InstallationRepairEquipment()
        elif equipment_type == EquipmentType.ASTEROID_MINING_ATTACHMENT:
            return AsteroidMiningAttachment()
        elif equipment_type == EquipmentType.RESOURCE_FACTORY_FRAME:
            return ResourceFactoryFrame()
        elif equipment_type == EquipmentType.ORBITAL_FACTORY_FRAME:
            return OrbitalFactoryFrame()
        elif equipment_type == EquipmentType.COMMUNICATIONS_ADAPTER:
            return CommunicationsAdapter()
        elif equipment_type == EquipmentType.PREJUDICE_TORPEDO_LAUNCHER:
            return PrejudiceTorpedoLauncher()
        elif equipment_type == EquipmentType.PULSE_BLAST_LASER:
            return PulseBlastLaser()
        elif equipment_type == EquipmentType.SONIC_BLASTER:
            return SonicBlaster()
        elif equipment_type == EquipmentType.COMPLETE_ARTIFACT:
            return CompleteArtifact()
        
        raise ValueError(f"Equipment type {equipment_type} not found")