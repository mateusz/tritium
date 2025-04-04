# Entities

## System

- System (abstract base for all planetary systems)
  - SolarSystem
  - StarSystem (non-Sun)

## Location

- Location (abstract base for all buildable locations)
  - Planet
  - Moon
  - Asteroid

## Base

- Base (buildable structure)
  - EarthBase (specific to only Earth)
  - OrbitalBase
  - ResourceBase (on surface)
  - MoonBase (specific to only Moon)

## Personnel

- Personnel (abstract base for all personnel)
  - Researcher
  - Marine
  - Producer

## Facility

- Facility (abstract base for all facilities, accessed in bases, cannot be stored)
  - Training
  - Research
  - Production
  - Mining
  - ShuttleBay
  - Spacedock (for IOS and SCG)
  - Storage
  - SelfDestructMechanism

## Vehicle

- Vehicle (abstract base for all vehicles)
  - Shuttle
  - IOS
  - SCG

## Equipment

- Equipment (abstract base for all equipment, all equipment can be built and stored in storage)
  - BaseEquipment (equipment installable on bases)
    - Derrick
    - SelfDestructMechanism
    - MassTransciever
    - AutoOperationsComputer
  - ShipEquipment (equipment installable on ship chassis)
    - AutoCargoComputer
    - DroneFleetControlComputer
    - IOSBattleDrone
    - StarDrone
    - Hyperspace (Hyperlight)
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
    - Tool (installable on ToolPod)
      - Grapple
      - InstallationRepairEquipment (Bandaid)
      - AsteroidMiningAttachment
      - ResourceFactoryFrame
      - OrbitalFactoryFrame
      - CommunicationsAdapter (COMMSPOD)
      - PrejudiceTorpedoLauncher
      - PulseBlastLaser
      - SonicBlaster
      - CompleteArtifact

## Grapplables (stuff that can be grappled)
- CommspodDesign
- Asteroid
- ArtifactPart
  
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
    - Apprentice
    - Engineer
    - Expert
  - ResearcherRank
    - Technician
    - Doctor
    - Professor
