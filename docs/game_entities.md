# Abstract Base Classes

## Location Types
- Base (abstract base for all bases)
  - EarthBase
  - OrbitalBase
  - SurfaceBase
  - MoonBase
- CelestialBody
  - Planet
  - Moon
  - Asteroid
- StarSystem
  - SolarSystem
  - FarStarSystem

## Personnel Types
- Personnel (abstract base for all personnel)
  - Researcher
  - Marine
  - Producer

## Facility Types
- Facility (abstract base for all facilities)
  - ResearchFacility
  - ProductionFacility
  - MiningFacility
  - ShuttleBay
  - SpaceBay
  - Spacedock
  - MiningStore
  - ResourceCenter
  - SelfDestructFacility
  - TeleporterFacility

## Vehicle Types
- Vehicle (abstract base for all vehicles)
  - Shuttle
  - IOS
  - SCG

## Equipment Types
- Equipment (abstract base for all equipment)
  - BaseEquipment (equipment installable on bases)
    - Derrick
    - SelfDestructMechanism
    - MassTransciever
    - AutoOperationsComputer
  
  - ShipEquipment (equipment installable on ship chassis)
    - AutoCargoComputer
    - DroneFleetControlComputer
    - BattleDrone
    - Chassis
      - ShuttleChassis
      - IOSChassis
      - SCGChassis
    - DriveUnit
      - ShuttleDrive
      - IOSDrive
      - SCGDrive
    - Pod
      - ResourcePod
      - ToolPod
      - CryoPod
      - PrisonPod
    - Tool
      - Grapple
      - InstallationRepairEquipment
      - AsteroidMiningAttachment
      - ResourceFactoryFrame
      - OrbitalFactoryFrame
      - CommunicationsAdapter
      - PrejudiceTorpedoLauncher
      - PulseBlastLaser
      - SonicBlaster
      - ArtifactPart
      - CompleteArtifact
  
## Resource Types
- Resource (abstract base for all resources)
  - Iron
  - Titanium
  - Aluminum
  - Copper
  - Palladium
  - Platinum
  - Silver
  - Gold
  - Hydrogen
  - Helium
  - Deuterium
  - Methane
  - Carbon
  - Silica
  - HydrogenMethanolFuel
  - HeliumDeuteriumFuel

## Rank Types
- Rank (abstract base for all ranks)
  - MarineRank
    - Pilot
    - Captain
    - Admiral
    - Warlord
  - ProducerRank
    - Technician
    - Doctor
    - Professor
  - ResearcherRank
    - Apprentice
    - Engineer
    - Expert
