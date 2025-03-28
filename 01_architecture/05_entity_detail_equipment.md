# Equipment Entity Details

## Equipment (Abstract Base)
The base class for all equipment in the game. All equipment can be stored in storage facilities and are used to enhance base and ship capabilities.

## BaseEquipment
Equipment that can be installed on bases to enhance their functionality.

### Derrick
Automated ore recovery and refining unit. Can adapt to all known elements and is semi-portable. Allows location on any mining site. Maximum of 8 derricks per resource base. 

### SelfDestructMechanism
Defensive equipment that can be installed in bases. Contains two switches (Cooling System and Reactor Control) that must be activated together to initiate a 12-second countdown. Can be used to destroy a base to prevent capture by Methanoids. Can also be used to disarm captured Methanoid bases.

### MassTransciever
Methanoid origin equipment that allows transmission of inanimate objects to any receiver. Technical analysis not understood. Requires two units to function - one at source and one at destination. Can be used to balance resources between bases or transport items instantly. Can transport minerals, tools, and equipment between any bases with transceivers.

### AutoOperationsComputer
Automates production processes, eliminating the need for Artisans. Can be programmed for on/off or repeating production. Yellow button indicates one-time production, green button indicates continuous production. Essential for automated drone production and resource management.

## ShipEquipment
Equipment that can be installed on ship chassis to enhance their capabilities.

### AutoCargoComputer
"Fit and Forget" system that allows programming of shuttles and IOS for automated stock haulage. Can be programmed to balance stocks between destinations. Cockpit mounted. Essential for automated resource transport between bases.

### DroneFleetControlComputer
Carried by fleet flagship. Controls fuel and drone dispersal. Automatically switches to combat mode when alien fleet detected. Takes up all 3 pod mountings on an IOS and 6 pod mountings on an SCG. Can control up to 200 drones in one fleet. Drones automatically go to the drone pool in space when built. Each drone adds 7 to fleet power (1400 total with 200 drones). Warlord pilots increase each drone's power by 3.

### IOSBattleDrone
Special chassis incorporating one fusion laser. Flight controlled via flagship drone computer installed on IOS. Used for combat operations against Methanoid forces. Can be deployed in fleets of up to 200 units. Each drone has a power of 7, unless commanded by the Warlord, in which case the power increases to 10. Note Methanoids can only use IOSBattleDrones at power 7, unaffecteed by rank.

### StarDrone
Similar to IOSBattleDrone, except can be installed on SCG. More expensive, but comes with a base power of 10. However if commanded by a pilot or captain, drone power goes down to 7.

### Hyperspace (Hyperlight)

Mentioned tangentially in a few places, it might be the faster-than-light drive for SCG that is discovered at some point?

### Chassis
Base ship frames that can be equipped with various components.

#### ShuttleChassis
Surface to orbit workhorse. Pod mounting allows maximum of 250 ton payload.

#### IOSChassis
Interplanetary operations spacecraft. Three pod mountings allow maximum of 750 ton payload. More advanced than shuttle chassis.

#### SCGChassis
Star Class Galleon. Methanoid Origin. Six pod mountings allow maximum of 1500 ton payload. Most advanced chassis in the game.

### DriveUnit
Propulsion systems for different ship types.

#### ShuttleDrive
Short burst drive which requires Hydrogen Methanol Fuel (MeH).

#### IOSDrive
Long duration drive unit. Requires Hydrogen Methanol Fuel.

#### SCGDrive
Fusion drive unit for interstellar travel. Methanoid origin. Requires Helium Deuterium Fuel (HeD).

### Pod
Specialized cargo containers that can be mounted on ships.

#### ResourcePod
For all material haulage. Standard fitted for use on a shuttle. Unit has a single cavity so may only hold one type of material. Maximum of 250 ton payload.

#### ToolPod
For haulage and mounting of tool or equipment. Mounting is linked to ship's cockpit allowing the crew to control any item carried.

#### CryoPod
For haulage of teams such as pilots or producers. Personnel are held in stasis while inside the pod. Protects occupants from disease and aging.

#### PrisonPod
Special pod for containing captured personnel. Can be used to imprison rogue captains or captured enemies. Locks when activated.

### Tool
Equipment that can be installed on ToolPods.

#### Grapple
For retrieving small objects of up to 250T. Must be pod mounted. Essential for asteroid capture and artifact recovery.

#### InstallationRepairEquipment (Bandaid)
For the repair of abandoned or derelict surface stations. Must be pod mounted. Requires operative shuttle bay.

#### AsteroidMiningAttachment
For surface mining of large asteroids. Process requires access to an empty supply pod. May be A.C.C. controlled. Asteroid must have a mass greater than 10,000 tons.

#### ResourceFactoryFrame
Partial framework for construction of surface stations. Computer control handles positioning sequence to ensure correct locking of the 2 sections.

#### OrbitalFactoryFrame
Partial framework for construction of orbital factories. Computer control handles positioning sequence to ensure correct locking of the 8 sections. Requires pilot on board for installation.

#### CommunicationsAdapter
Methanoid origin. Translates verbal communication into HUD text. Technical Analysis also reveals holographic image processing.

#### PrejudiceTorpedoLauncher
Fires a torpedo loaded with 100T of fuel from the host ship tanks. Detonation is triggered when the predicted outcome is prejudiced against enemy drones. Cockpit mounted. Can fire two torpedoes with full fuel.

#### PulseBlastLaser
Highly destructive pulse weapon. Requires at least 3 chassis units for correct operation. Awesome weapon for defending factories. Destroys both enemy drones and the ship carrying it. Does not require pilots but cannot be flown once installed.

#### SonicBlaster
Methanoid origin. Fusion powered unit. Emits pulses at present intervals and frequencies. Power adjuster fitted. Not actually a weapon despite being labeled as one - functions as a music player.

