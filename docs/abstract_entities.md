# Abstract Base Classes and Their Relationships

## Abstract Base Classes

### Location Types
- Base
- CelestialBody
- StarSystem

### Personnel Types
- Personnel

### Facility Types
- Facility

### Vehicle Types
- Vehicle

### Equipment Types
- Equipment
  - BaseEquipment
  - ShipEquipment
    - Chassis
    - DriveUnit
    - Pod
    - Tool

### Resource Types
- Resource

### Rank Types
- Rank

## Entity Relationships

### Base
- has_many: Facilities
- has_many: Personnel
- has_many: BaseEquipment
- has_one: CelestialBody (location)

### CelestialBody
- has_many: Bases
- has_many: Resources
- belongs_to: StarSystem

### StarSystem
- has_many: CelestialBodies
- has_many: Bases

### Personnel
- belongs_to: Base
- has_one: Rank

### Facility
- belongs_to: Base
- has_many: Personnel (if it's a manned facility)
- has_many: BaseEquipment (if it can have equipment installed)

### Vehicle
- has_one: Chassis
- has_one: DriveUnit
- has_many: Pods
- has_many: Tools
- has_many: ShipEquipment