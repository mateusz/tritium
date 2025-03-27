#!/usr/bin/env python3
import random
from dataclasses import dataclass
from typing import List, Tuple, Dict, Literal
import statistics
import argparse

# Global randomness parameters
INITIAL_LUCK_MIN = 0.6  # Minimum initial luck factor
INITIAL_LUCK_MAX = 1.4  # Maximum initial luck factor
BASE_DAMAGE_MIN = 0.1   # Minimum base damage percentage
BASE_DAMAGE_MAX = 0.15  # Maximum base damage percentage
DAMAGE_RANDOM_MIN = 0.7  # Minimum damage randomness multiplier
DAMAGE_RANDOM_MAX = 1.3  # Maximum damage randomness multiplier
LUCK_UPDATE_MIN = 0.95  # Minimum luck update factor
LUCK_UPDATE_MAX = 1.05  # Maximum luck update factor

@dataclass
class Fleet:
    """Represents a drone fleet in battle"""
    name: str
    drones: int
    drone_type: Literal["IOS", "Star"]
    pilot_rank: Literal["None", "Admiral", "Warlord"]
    
    def calculate_power(self) -> int:
        """Calculate the total power of the fleet based on drone type and pilot rank"""
        base_power = 7 if self.drone_type == "IOS" else 10
        
        # Star Drones ignore pilot rank modifier
        if self.drone_type == "Star":
            return base_power * self.drones
            
        # Apply pilot rank modifier for IOS drones
        pilot_bonus = 0
        if self.pilot_rank == "Admiral":
            pilot_bonus = 3
        elif self.pilot_rank == "Warlord":
            pilot_bonus = 6
            
        return (base_power + pilot_bonus) * self.drones


def simulate_battle(attacker: Fleet, defender: Fleet, random_seed: int = None) -> Tuple[Fleet, Fleet, str, int]:
    """
    Simulate a battle between two fleets.
    
    Args:
        attacker: The attacking fleet
        defender: The defending fleet
        random_seed: Optional seed for reproducibility
        
    Returns:
        Tuple of (updated attacker fleet, updated defender fleet, winner name, battle rounds)
    """
    # Clone the fleets to avoid modifying the originals
    attacker = Fleet(
        name=attacker.name,
        drones=attacker.drones,
        drone_type=attacker.drone_type,
        pilot_rank=attacker.pilot_rank
    )
    
    defender = Fleet(
        name=defender.name,
        drones=defender.drones,
        drone_type=defender.drone_type,
        pilot_rank=defender.pilot_rank
    )
    
    # Set random seed if provided
    if random_seed is not None:
        random.seed(random_seed)
    
    # Battle parameters
    battle_round = 1
    max_rounds = 100
    
    # Initial luck factor (random advantage based on global parameters)
    attacker_luck = random.uniform(INITIAL_LUCK_MIN, INITIAL_LUCK_MAX)
    defender_luck = random.uniform(INITIAL_LUCK_MIN, INITIAL_LUCK_MAX)
    
    # Main battle loop
    while battle_round <= max_rounds:
        # Calculate round power with random luck factor
        attacker_power = attacker.calculate_power() * attacker_luck
        defender_power = defender.calculate_power() * defender_luck
        
        # Calculate normalized power ratio (always between 0.5 and 2.0)
        if attacker_power >= defender_power:
            power_ratio = 1.0 + min(0.5, (attacker_power - defender_power) / defender_power)
        else:
            power_ratio = 1.0 / (1.0 + min(0.5, (defender_power - attacker_power) / attacker_power))
        
        # Base damage is a percentage of current drones
        # For equal power, each side loses about BASE_DAMAGE_MIN to BASE_DAMAGE_MAX % of their drones per round
        base_damage_percent = random.uniform(BASE_DAMAGE_MIN, BASE_DAMAGE_MAX)
        
        # Apply power ratio to damage
        if power_ratio >= 1.0:  # Attacker advantage
            attacker_loss_percent = base_damage_percent / power_ratio
            defender_loss_percent = base_damage_percent * power_ratio
        else:  # Defender advantage
            attacker_loss_percent = base_damage_percent / power_ratio
            defender_loss_percent = base_damage_percent * power_ratio
        
        # Add randomness to damage based on global parameters
        attacker_damage_rand = random.uniform(DAMAGE_RANDOM_MIN, DAMAGE_RANDOM_MAX)
        defender_damage_rand = random.uniform(DAMAGE_RANDOM_MIN, DAMAGE_RANDOM_MAX)
        
        # Calculate actual drone losses
        attacker_loss = round(attacker.drones * attacker_loss_percent * attacker_damage_rand)
        defender_loss = round(defender.drones * defender_loss_percent * defender_damage_rand)
        
        # Ensure minimum damage
        attacker_loss = max(1, attacker_loss) if attacker.drones > 1 else attacker.drones
        defender_loss = max(1, defender_loss) if defender.drones > 1 else defender.drones
        
        # Add proportional damage cap for highly unbalanced fleet sizes
        # This prevents excessively high casualties in a large fleet when fighting a small one
        if attacker.drones >= 5 * defender.drones:
            # Cap attacker losses proportionally to defender size
            attacker_loss = min(attacker_loss, max(1, round(defender.drones * 0.5)))
        elif defender.drones >= 5 * attacker.drones:
            # Cap defender losses proportionally to attacker size
            defender_loss = min(defender_loss, max(1, round(attacker.drones * 0.5)))
        
        # Apply damage
        attacker.drones -= attacker_loss
        defender.drones -= defender_loss
        
        # Ensure no negative drones
        attacker.drones = max(0, attacker.drones)
        defender.drones = max(0, defender.drones)
        
        # Check for battle end conditions
        if attacker.drones <= 0 or defender.drones <= 0:
            break
        
        # Update luck factor for next round using global parameters
        attacker_luck *= random.uniform(LUCK_UPDATE_MIN, LUCK_UPDATE_MAX)
        defender_luck *= random.uniform(LUCK_UPDATE_MIN, LUCK_UPDATE_MAX)
        
        # Keep luck factor within bounds
        attacker_luck = max(INITIAL_LUCK_MIN, min(INITIAL_LUCK_MAX, attacker_luck))
        defender_luck = max(INITIAL_LUCK_MIN, min(INITIAL_LUCK_MAX, defender_luck))
        
        battle_round += 1
    
    # Determine the winner
    winner = ""
    if attacker.drones <= 0 and defender.drones <= 0:
        # Both destroyed - 50/50 chance
        winner = random.choice([attacker.name, defender.name])
    elif attacker.drones <= 0:
        winner = defender.name
    elif defender.drones <= 0:
        winner = attacker.name
    else:
        # Max rounds reached - compare remaining drones
        if attacker.drones > defender.drones:
            winner = attacker.name
        elif defender.drones > attacker.drones:
            winner = defender.name
        else:
            # Equal drones - defender wins (home advantage)
            winner = defender.name
    
    return attacker, defender, winner, battle_round


def run_simulations(attacker: Fleet, defender: Fleet, num_simulations: int = 1000) -> Dict:
    """
    Run multiple battle simulations and collect statistics
    
    Args:
        attacker: The attacking fleet
        defender: The defending fleet
        num_simulations: Number of simulations to run
        
    Returns:
        Dictionary with statistics about the battle results
    """
    results = {
        "attacker_wins": 0,
        "defender_wins": 0,
        "attacker_remaining_drones": [],
        "defender_remaining_drones": [],
        "battle_rounds": []
    }
    
    for i in range(num_simulations):
        # Generate a unique seed for each simulation for reproducibility
        seed = i + 1000  # Different base seed to avoid any patterns
        
        # Run the simulation
        final_attacker, final_defender, winner, rounds = simulate_battle(
            attacker, defender, random_seed=seed
        )
        
        # Update statistics
        if winner == attacker.name:
            results["attacker_wins"] += 1
        else:
            results["defender_wins"] += 1
            
        results["attacker_remaining_drones"].append(final_attacker.drones)
        results["defender_remaining_drones"].append(final_defender.drones)
        results["battle_rounds"].append(rounds)
    
    # Calculate percentages
    total_simulations = results["attacker_wins"] + results["defender_wins"]
    results["attacker_win_percent"] = (results["attacker_wins"] / total_simulations) * 100
    results["defender_win_percent"] = (results["defender_wins"] / total_simulations) * 100
    
    # Calculate averages and medians for remaining drones
    results["avg_attacker_remaining"] = statistics.mean(results["attacker_remaining_drones"])
    results["avg_defender_remaining"] = statistics.mean(results["defender_remaining_drones"])
    results["median_attacker_remaining"] = statistics.median(results["attacker_remaining_drones"])
    results["median_defender_remaining"] = statistics.median(results["defender_remaining_drones"])
    results["avg_battle_rounds"] = statistics.mean(results["battle_rounds"])
    
    return results


def print_simulation_results(test_case: str, attacker: Fleet, defender: Fleet, results: Dict):
    """Print formatted simulation results"""
    print(f"\n{'=' * 70}")
    print(f"TEST CASE: {test_case}")
    print(f"{'=' * 70}")
    
    print(f"ATTACKER: {attacker.name}")
    print(f"  - Drones: {attacker.drones} {attacker.drone_type}")
    print(f"  - Pilot: {attacker.pilot_rank}")
    print(f"  - Initial Power: {attacker.calculate_power()}")
    
    print(f"\nDEFENDER: {defender.name}")
    print(f"  - Drones: {defender.drones} {defender.drone_type}")
    print(f"  - Pilot: {defender.pilot_rank}")
    print(f"  - Initial Power: {defender.calculate_power()}")
    
    print(f"\nRESULTS (after {len(results['attacker_remaining_drones'])} simulations):")
    print(f"  - Attacker Win Rate: {results['attacker_win_percent']:.2f}%")
    print(f"  - Defender Win Rate: {results['defender_win_percent']:.2f}%")
    print(f"  - Average Attacker Remaining Drones: {results['avg_attacker_remaining']:.2f}")
    print(f"  - Average Defender Remaining Drones: {results['avg_defender_remaining']:.2f}")
    print(f"  - Median Attacker Remaining Drones: {results['median_attacker_remaining']}")
    print(f"  - Median Defender Remaining Drones: {results['median_defender_remaining']}")
    print(f"  - Average Battle Rounds: {results['avg_battle_rounds']:.2f}")


def define_test_cases() -> List[Tuple[str, Fleet, Fleet]]:
    """Define test cases including normal scenarios and edge cases"""
    test_cases = []
    
    # Test Case 1: Example from documentation - Admiral vs Warlord
    test_cases.append((
        "Admiral vs Warlord (Example from docs)",
        Fleet(name="IOS Admiral", drones=200, drone_type="IOS", pilot_rank="Admiral"),
        Fleet(name="IOS Warlord", drones=200, drone_type="IOS", pilot_rank="Warlord")
    ))
    
    # Test Case 2: Equal fleets with equal pilots
    test_cases.append((
        "Equal IOS fleets with Admiral pilots",
        Fleet(name="IOS Admiral 1", drones=200, drone_type="IOS", pilot_rank="Admiral"),
        Fleet(name="IOS Admiral 2", drones=200, drone_type="IOS", pilot_rank="Admiral")
    ))
    
    # Test Case 3: Different drone types
    test_cases.append((
        "IOS vs Star drones - equal counts",
        Fleet(name="IOS Fleet", drones=200, drone_type="IOS", pilot_rank="None"),
        Fleet(name="Star Fleet", drones=200, drone_type="Star", pilot_rank="None")
    ))
    
    # Test Case 4: Different fleet sizes
    test_cases.append((
        "Different fleet sizes - same drone type",
        Fleet(name="Large Fleet", drones=200, drone_type="IOS", pilot_rank="None"),
        Fleet(name="Small Fleet", drones=100, drone_type="IOS", pilot_rank="None")
    ))
    
    # Test Case 5: Edge case - minimum fleet size
    test_cases.append((
        "Edge case - minimum fleet size",
        Fleet(name="Minimal Fleet", drones=1, drone_type="IOS", pilot_rank="None"),
        Fleet(name="Standard Fleet", drones=100, drone_type="IOS", pilot_rank="None")
    ))
    
    # Test Case 6: Max power difference
    test_cases.append((
        "Max power difference - Star Warlord vs IOS None",
        Fleet(name="Max Star", drones=200, drone_type="Star", pilot_rank="Warlord"),
        Fleet(name="Basic IOS", drones=200, drone_type="IOS", pilot_rank="None")
    ))
    
    # Test Case 7: Nearly identical power
    test_cases.append((
        "Nearly identical total power",
        Fleet(name="IOS Warlord", drones=100, drone_type="IOS", pilot_rank="Warlord"),
        Fleet(name="Star Fleet", drones=130, drone_type="Star", pilot_rank="None")
    ))

    # Test Case 8: Very small fleets
    test_cases.append((
        "Very small fleets with high rank pilots",
        Fleet(name="Small Warlord", drones=10, drone_type="IOS", pilot_rank="Warlord"),
        Fleet(name="Small Admiral", drones=10, drone_type="IOS", pilot_rank="Admiral")
    ))

    return test_cases


def create_custom_fleet(
    name: str, 
    drones: int, 
    drone_type: str, 
    pilot_rank: str
) -> Fleet:
    """Create a custom fleet based on user inputs"""
    # Validate drone count
    drones = max(1, min(200, drones))
    
    # Validate drone type
    if drone_type.upper() not in ["IOS", "STAR"]:
        print(f"Invalid drone type: {drone_type}. Using IOS as default.")
        drone_type = "IOS"
    else:
        drone_type = drone_type.upper()
    
    # Validate pilot rank
    if pilot_rank.upper() not in ["NONE", "ADMIRAL", "WARLORD"]:
        print(f"Invalid pilot rank: {pilot_rank}. Using None as default.")
        pilot_rank = "None"
    else:
        pilot_rank = pilot_rank.capitalize()
        if pilot_rank == "None":
            pilot_rank = "None"  # Preserve case for None
    
    return Fleet(name=name, drones=drones, drone_type=drone_type, pilot_rank=pilot_rank)



def main():
    """Main function to run the simulation"""
    
    print("DEUTEROS BATTLE SIMULATOR")
    print("------------------------")
    
    # Run all test cases
    test_cases = define_test_cases()
    for test_case, attacker, defender in test_cases:
        results = run_simulations(attacker, defender, 1000)
        print_simulation_results(test_case, attacker, defender, results)


if __name__ == "__main__":
    main() 