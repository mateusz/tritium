# System Entity Details

## System (Abstract Base)
The base class for all planetary systems in the game. Systems represent different star systems that can be explored and colonized.

## SolarSystem
Represents the Sol system (our solar system). This is the starting system where players begin their journey. Contains familiar planets like Earth, Moon, Mars, Venus, etc. The first major battleground against the Methanoids.

## StarSystem (Non-Sun)
Represents other star systems beyond Sol that can be explored and colonized. Examples include Proxima, Pacific, and Barent. These systems become accessible after developing advanced space travel technology. Each system contains its own planets, resources, and Methanoid bases that need to be conquered. The game requires conquering 7 of these systems to win.

# Location Entity Details

## Location (Abstract Base)
The base class for all buildable locations in the game. Locations represent celestial bodies where players can establish bases and mining operations.

## Planet
A major celestial body that can host both orbital and surface bases. Planets can have moons orbiting them. Each planet has unique resource deposits that can be mined. Examples include Earth, Mars, Venus, and the gas giants. Planets are key strategic locations for establishing both orbital factories and surface resource bases.

## Moon
A smaller celestial body orbiting a planet. Can host both orbital and surface bases, though typically smaller in scale than planets. Examples include Earth's Moon, Leda, Callisto, and Titan. Moons often have unique resource deposits and can be important strategic locations for establishing bases.

## Asteroid
Small celestial bodies that can be mined for resources. Found in asteroid belts between planets (notably between Mars and Jupiter). Can be captured and mined using specialized equipment like grapples and asteroid mining attachments. Important source of rare resources like silver and platinum. Asteroids have a mass limit of 250 tons for capture and processing with grapple, but ships can land and mine bigger ones.

# Base Entity Details

## Base (Abstract Base)
The base class for all buildable structures in the game. Bases are the primary facilities where production, research, and resource management occur.

## EarthBase
A special base type that can only be built on Earth. The starting point of the game where players begin their journey. Contains the initial research, production, and training facilities. The only base that can train new personnel and do research throughout the entire game.

## OrbitalBase
A space station built in orbit around a celestial body. Constructed from 8 orbital factory sections. Can host production facilities, research labs, and storage. Requires personnel to be transported via cryo pods to become operational. Has various facilities like shuttle bays, spacedocks, and self-destruct mechanisms.

## ResourceBase
A surface base built on planets or moons. Constructed from 2 resource frames. Used for mining and resource extraction. Can be equipped with derricks for automated resource gathering. Maximum of 8 derricks per resource base. Resources can be transported to orbital bases using shuttle systems.

## MoonBase
A special base type that can only be built on Earth's Moon. Represents the rediscovered original moon base from the previous game (Millennium). Has unique historical significance in the game's lore. Needs only be repaired.

# Personnel Entity Details

## Personnel (Abstract Base)
The base class for all personnel types in the game. Personnel are the workers, researchers, and military personnel that operate bases and ships.

## Researcher
Scientific personnel responsible for researching new technologies and items. Can be trained at EarthBase. Maximum team size of 250 researchers. Has three ranks: Technician, Doctor, and Professor. Higher ranks are required for researching more advanced technologies. Researchers are essential for game progression as they unlock new items and technologies.

## Marine
Military personnel who can pilot ships and command drone fleets. Can be trained at EarthBase. Maximum team size of 41 marines. Has four ranks: Pilot, Captain, Admiral, and Warlord. Higher ranks provide significant combat bonuses - Admirals increase drone power by 3, while Warlords increase it by 6. Essential for combat operations and ship command.

## Producer
Industrial personnel responsible for manufacturing items and operating production facilities. Can be trained at EarthBase. Maximum team size of 200 producers. Has three ranks: Apprentice, Engineer, and Expert. Higher ranks enable production of more advanced items. Producers are crucial for building ships, equipment, and maintaining base operations.

# Facility Entity Details

## Facility (Abstract Base)
The base class for all facilities that can be built within bases. Facilities are permanent installations that cannot be stored and are accessed directly within bases.

## Training
Facility for training new personnel. Located in EarthBase. Contains three training doors for recruiting different types of personnel: researchers, producers, and marines. Each door can train up to its maximum team size (250 researchers, 200 producers, 41 marines). Doors close during training and reopen when training is complete. There is also a quirky light switch that... switches the light on and off in the room.

## Research
Facility for researching new technologies and items. Located in EarthBase. Contains a list of researchable items with status indicators (red for available, yellow for in progress, green for completed). Shows research progress percentage, tech level, and resource requirements for each item. Higher researcher ranks are required for advanced research.

## Production
Facility for manufacturing items and equipment. Available in both EarthBase and OrbitalBase. Shows a list of producible items with status indicators (green for available, red for unavailable due to rank, yellow for orbital-only). Displays leader name, rank, and staff count. Can be automated using Auto Operations Computer (AOC).

## Mining
Facility for resource extraction and management. Located in any Base. Controls up to 8 derricks for automated resource gathering. Shows current mining operations and resources remaining. Resources can be automatically transported to orbital bases using shuttle systems.

## ShuttleBay
Facility for managing shuttles. Located in bases. Used for building new shuttles, equipping them, assigning crew, and refueling. Contains sections for crew assignment, pod mounting, and engine installation. Can service and maintain shuttles when they are docked.

## Spacedock
Facility for managing IOS (Interplanetary Operations Spacecraft) and SCG (Star Class Galleon) ships. Similar to ShuttleBay but specialized for larger vessels. Used for building, equipping, and maintaining these advanced ships. Located in OrbitalBase only.

## Storage
Facility for managing resources and equipment. Available in all bases. Shows current inventory of Equipment. Can be accessed through the Stocktaker interface.

## SelfDestructMechanism
Defensive facility that can be installed in bases. Contains two switches (Cooling System and Reactor Control) that must be activated together to initiate a 12-second countdown. Can be used to destroy a base to prevent capture by Methanoids. Can also be used to disarm captured Methanoid bases.

# Vehicle Entity Details

## Vehicle (Abstract Base)
The base class for all vehicles in the game. Vehicles are mobile units that can transport personnel, resources, and equipment between locations.

## Shuttle
The basic spacecraft used for surface-to-orbit operations. Can carry up to 250 tons of cargo in a single pod. Requires a pilot and can be equipped with various pods (supply, tool, team). Uses Hydrogen Methanol Fuel (MeH). Can be automated with Auto Cargo Computer (ACC) for resource transport. Limited to traveling between surface and orbital bases.

## IOS (Interplanetary Operations Spacecraft)
Advanced spacecraft capable of interplanetary travel. Has three pod mountings allowing up to 750 tons of cargo. Can be equipped with Auto Cargo Computer (ACC) and Drone Fleet Control Computer (DFCC). Uses Hydrogen Methanol Fuel (MeH). Can travel between any planets in the solar system. Essential for combat operations and resource transport.

## SCG (Star Class Galleon)
The most advanced spacecraft, capable of interstellar travel. Has six pod mountings allowing up to 1500 tons of cargo. Can be equipped with Drone Fleet Control Computer (DFCC) for controlling star drones. Uses Helium Deuterium Fuel (HeD). Can travel between different star systems. The most powerful combat vessel in the game.

# Rank Entity Details

## Rank (Abstract Base)
The base class for all personnel ranks in the game. Ranks determine personnel capabilities and access to advanced features.

## MarineRank
Military personnel ranks that affect combat capabilities and ship command.

### Pilot
Entry-level rank for marines. Can pilot basic ships and perform basic combat operations.

### Captain
Mid-level rank for marines. Improved combat capabilities and ship command abilities.

### Admiral
Advanced rank for marines. Provides significant combat bonuses - increases drone power by 3. Can command larger fleets and access advanced combat features.

### Warlord
Highest rank for marines. Provides maximum combat bonuses - increases drone power by 6. Can be achieved by traveling faster than light with an Admiral. Essential for late-game combat operations.

## ProducerRank
Industrial personnel ranks that affect production capabilities.

### Apprentice
Entry-level rank for producers. Can produce basic items and equipment.

### Engineer
Mid-level rank for producers. Can produce more advanced items and equipment.

### Expert
Highest rank for producers. Can produce all available items and equipment. Required for some advanced manufacturing.

## ResearcherRank
Scientific personnel ranks that affect research capabilities.

### Technician
Entry-level rank for researchers. Can research basic technologies and items.

### Doctor
Mid-level rank for researchers. Can research more advanced technologies and items.

### Professor
Highest rank for researchers. Can research all available technologies and items. Required for the most advanced research projects.