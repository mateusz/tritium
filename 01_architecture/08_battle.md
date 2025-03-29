# Battle Mechanics

## Overview
Battles in Deuteros occur when Methanoid forces attack player bases or when player forces attack Methanoid bases. The core of the battle system revolves around drone fleets controlled by special computers.

## Fleet Composition

### Drone Types
1. IOS Battle Drone
   - Base power: 7
   - Can be controlled by IOS ships
   - Maximum 200 drones per fleet
   - Total fleet power: 1400 (200 * 7)

2. Star Drone
   - Base power: 10
   - Can be controlled by SCG ships
   - Maximum 200 drones per fleet
   - Total fleet power: 2000 (200 * 10)

### Fleet Control
- Fleet Control Computer takes up:
  - All 3 pod mountings on an IOS
  - All 6 pod mountings on an SCG
- Maximum of 200 drones per fleet
- Drones automatically go to drone pool in space when built
- Fleet power is calculated by summing individual drone powers

### Pilot Ranks and Power Modifiers
- Warlord pilots increase IOS drone power by 3 (from 7 to 10)
- Warlord pilots do not affect Star drone power (stays at 10)
- Methanoids can only use IOS Battle Drones at base power (7), unaffected by rank

## Battle Algorithm

1. Fleet Formation
   - Each side forms up to 200 drones into a fleet
   - Fleet power is calculated based on drone types and pilot ranks
   - Drones are represented on the battle map as red (enemy) and green (player)

2. Battle Initiation
   - Battle begins when fleets are in range of each other
   - Each fleet starts with full strength (200 drones)
   - Battle continues until one side is defeated, or retreats (which immediately stops the battle)

3. Combat Resolution
   - Fleets engage in direct combat
   - Drones are lost based on relative fleet strengths
   - Battle continues in rounds until one side is defeated
   - Victory is achieved when enemy fleet is destroyed

4. Special Weapons
   - Prejudice Torpedo Launcher can be used during battle
   - Fires torpedo loaded with 100T of fuel
   - Most effective when enemy drones are closely packed
   - Can fire two torpedoes with full fuel
   - Each torpedo can significantly reduce enemy drone numbers

5. Battle Outcomes
   - Defeat: All drones lost
   - Victory: Enemy fleet destroyed
   - Base capture possible after fleet victory
