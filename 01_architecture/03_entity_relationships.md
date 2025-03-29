# Entity Relationships

### System
- has-many: Location
- has-many: Base
- has-many: Vehicle

### Location
- has-one: System
- has-one: Base
- has-many: Resource
- has-many: Vehicle

### Base
- has-one: System
- has-one: Location
- has-many: Facility
- has-many: Personnel
- has-one: Vehicle (in ShuttleBay)
- has-one: Vehicle (in Spacedock)
- has-many: Equipment
- has-many: Resource

### Personnel
- has-one: Base
- has-one: Rank
- has-one: Vehicle (if assigned as pilot/crew)
- has-one: CryoPod (if in cryo pod)

### Facility
- has-one: Base
- has-many: Personnel

### Vehicle
- has-one: System
- has-one: Location
- has-one: Base (if docked)
- has-one: Personnel (crew)
- has-many: Equipment (installable)
- has-many: Artifact (installable)