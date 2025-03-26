# Entity Relationships

1. Base Relationships:
   - Has many Facility
   - Has many Vehicle (docked)
   - Has many Personnel (stationed)
   - Has many Resource (stored)
   - Has many Equipment (stored)
   - Has many Equipment (installed)
   - Has one Base (paired orbital or surface base)
   - Has one Shuttle (dedicated shuttle)

2. CelestialBody Relationships:
   - Has one Base
   - Has many Resource (natural deposits)

3. StarSystem Relationships:
   - Has many CelestialBodies

4. Personnel Relationships:
   - Has one Rank

5. Vehicle Relationships:
   - Has many Equipment (installed)
   - Has one pilot
   - Has one base (currently stationed in)

6. Facility Relationships:
   - TODO