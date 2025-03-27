# Battle Mechanics

## Overview
Battles in Deuteros are primarily fought using drone fleets controlled by ships equipped with Drone Fleet Control Computers (DFCC). The battle system is turn-based and involves strategic positioning and management of drone fleets.

## Fleet Composition

### Drone Types
1. IOS Battle Drones
   - Base power: 7 per drone
   - Maximum fleet size: 200 drones (1400 total power)
   - Can only be used in solar system battles
   - Controlled by IOS ships with DFCC

2. Star Drones
   - Base power: 10 per drone
   - Maximum fleet size: 200 drones (2000 total power)
   - Can be used in interstellar battles
   - Controlled by SCG ships with DFCC

### Fleet Power Modifiers
- Admiral pilot: +3 power per drone
- Warlord pilot: +6 power per drone
- Star Drones maintain 10 power regardless of pilot rank

## Battle Mechanics

### Fleet Control
1. Ships must be equipped with DFCC to control drones
   - IOS: Takes up all 3 pod mountings
   - SCG: Takes up all 6 pod mountings

2. Drone Management
   - Drones are stored in a pool when built
   - Must be manually added to fleet (up to 200)
   - Can be removed from fleet back to pool
   - Fleet power is calculated based on drone count and pilot rank

### Combat Resolution
1. Battle Initiation
   - Methanoids attack bases with 4 days warning
   - Player must position defending fleet within 4 days
   - Maximum Methanoid fleet power in solar system: 1400

2. Battle Process
   - Fleets engage in combat when in range
   - Power comparison determines battle outcome
   - Higher power fleet typically wins
   - Torpedoes can be used when fleets are closely packed
     - Cost: 100T fuel per shot
     - Maximum 2 shots with full fuel
     - Reduces enemy fleet by ~90 drones
     - Reduces friendly fleet by ~15 drones

3. Special Weapons
   - Prejudice Torpedo Launcher: Strategic weapon for fleet combat
   - Pulse Blast Laser: Defensive weapon that destroys both enemy drones and carrier ship
   - Sonic Blaster: Non-combat device (plays music)

## Battle Algorithm

### Fleet Power Calculation
1. Base Fleet Power
   - IOS Drones: 7 × number_of_drones
   - Star Drones: 10 × number_of_drones

2. Pilot Rank Modifier
   - Admiral: +3 power per drone
   - Warlord: +6 power per drone
   - Star Drones ignore pilot rank modifier

3. Final Fleet Power Formula
   ```
   For IOS Drones:
   total_power = (7 + pilot_rank_bonus) × number_of_drones
   
   For Star Drones:
   total_power = 10 × number_of_drones
   ```

### Battle Resolution Algorithm
1. Initial Setup
   - Calculate total power for both fleets
   - Initialize battle_round = 1
   - Set max_rounds = 10
   - Set random_seed based on game state for reproducibility

2. Main Battle Loop
   ```
   while battle_round <= max_rounds:
       # Check for torpedo usage
       if fleets_are_closely_packed and torpedo_available:
           apply_torpedo_effects()
           continue
       
       # Calculate round damage
       attacker_power = calculate_fleet_power(attacker)
       defender_power = calculate_fleet_power(defender)
       
       # Calculate base damage with power difference
       power_difference = abs(attacker_power - defender_power)
       base_damage = power_difference / 10
       
       # Apply random variance to damage
       random_factor = random(0.8, 1.2)  # ±20% variance
       attacker_damage = base_damage * random_factor
       defender_damage = base_damage * random_factor * 0.5  # Defender takes half damage
       
       # Apply damage with randomness
       if attacker_power > defender_power:
           defender_drones -= round(attacker_damage)
           attacker_drones -= round(defender_damage)
       else:
           attacker_drones -= round(attacker_damage)
           defender_drones -= round(defender_damage)
       
       # Ensure no negative drones
       defender_drones = max(0, defender_drones)
       attacker_drones = max(0, attacker_drones)
       
       # Check for battle end conditions
       if attacker_drones <= 0 or defender_drones <= 0:
           return determine_winner()
       
       battle_round += 1
   ```

3. Torpedo Effects
   ```
   def apply_torpedo_effects():
       if torpedo_fuel >= 100:
           # Apply random variance to torpedo damage
           enemy_random = random(0.85, 1.15)  # ±15% variance
           friendly_random = random(0.9, 1.1)  # ±10% variance
           
           enemy_drones -= round(90 * enemy_random)
           friendly_drones -= round(15 * friendly_random)
           torpedo_fuel -= 100
   ```

4. Battle End Conditions
   - Winner is determined by:
     - First fleet to reach 0 drones loses
     - If both fleets survive max_rounds, winner is fleet with more remaining drones
     - If equal drones remain, defender wins (home advantage)
     - In case of exact tie, random chance (50/50) determines winner

5. Special Cases
   - Pulse Blast Laser: Immediately destroys both fleets and carrier ship
   - Maximum Methanoid fleet power in solar system is capped at 1400
   - Star Drones maintain constant power regardless of pilot rank
   - Random seed is preserved for save/reload consistency

### Example Battle
```
Attacker: 200 IOS Drones with Admiral (+3 power)
Defender: 200 IOS Drones with Warlord (+6 power)

Initial Power:
- Attacker: (7 + 3) × 200 = 2000 power
- Defender: (7 + 6) × 200 = 2600 power

Round 1:
- Defender has advantage
- Power difference: 2600 - 2000 = 600
- Base damage: 600 / 10 = 60
- Random factors: 0.95 (attacker), 1.05 (defender)
- Attacker loses: round(60 * 0.95) = 57 drones
- Defender loses: round(60 * 0.95 * 0.5) = 29 drones
- Remaining: Attacker 143, Defender 171

Battle continues until one fleet is destroyed or max rounds reached
```
