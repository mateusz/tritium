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
   - Battle continues until one side is defeated

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

## Battle Outcome Calculation

```python
import random
from typing import Tuple

def calculate_fleet_power(drone_count: int, drone_type: str, pilot_rank: str) -> int:
    """
    Calculate total fleet power based on drone count, type and pilot rank.
    Methanoids always use IOS drones at base power (7).
    """
    if drone_type == "IOS":
        base_power = 7
        if pilot_rank == "Warlord":
            base_power += 3  # Warlord bonus only applies to IOS drones
    else:  # Star Drone
        base_power = 10  # Star drones always at 10, unaffected by rank
    
    return drone_count * base_power

def resolve_battle(
    player_drone_count: int,
    player_drone_type: str,
    player_pilot_rank: str,
    methanoid_drone_count: int
) -> Tuple[bool, int, int]:
    """
    Resolve a battle between player and Methanoid fleets.
    Returns: (player_victory, player_drones_lost, methanoid_drones_lost)
    """
    # Calculate fleet powers
    player_power = calculate_fleet_power(player_drone_count, player_drone_type, player_pilot_rank)
    methanoid_power = calculate_fleet_power(methanoid_drone_count, "IOS", "None")  # Methanoids always use IOS drones
    
    # Calculate power ratio (0.0 to 1.0)
    total_power = player_power + methanoid_power
    player_ratio = player_power / total_power
    
    # Add some randomness (10% variance)
    random_factor = random.uniform(0.9, 1.1)
    adjusted_ratio = player_ratio * random_factor
    
    # Determine winner based on adjusted ratio
    player_victory = adjusted_ratio > 0.5
    
    # Calculate losses (roughly proportional to enemy power)
    if player_victory:
        # Player wins - lose fewer drones
        player_losses = int(methanoid_drone_count * (1 - player_ratio) * random.uniform(0.7, 0.9))
        methanoid_losses = methanoid_drone_count  # Methanoids lose all drones
    else:
        # Methanoids win - lose fewer drones
        player_losses = player_drone_count  # Player loses all drones
        methanoid_losses = int(player_drone_count * player_ratio * random.uniform(0.7, 0.9))
    
    return player_victory, player_losses, methanoid_losses

# Example usage:
# player_victory, player_losses, methanoid_losses = resolve_battle(
#     player_drone_count=200,
#     player_drone_type="IOS",
#     player_pilot_rank="Warlord",
#     methanoid_drone_count=200
# )
```
