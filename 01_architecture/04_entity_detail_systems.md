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

