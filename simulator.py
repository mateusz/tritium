import random
from typing import Tuple, List
from collections import defaultdict
from dataclasses import dataclass
from statistics import mean, stdev

@dataclass
class BattleResult:
    player_victory: bool
    player_losses: int
    methanoid_losses: int
    player_drone_type: str
    player_pilot_rank: str
    player_drone_count: int
    methanoid_drone_count: int

def calculate_fleet_power(drone_count: int, drone_type: str, pilot_rank: str) -> int:
    """Calculate total fleet power based on drone count, type and pilot rank."""
    if drone_type == "IOS":
        base_power = 7
        if pilot_rank == "Warlord":
            base_power += 3
    else:  # Star Drone
        base_power = 10
    return drone_count * base_power

def resolve_battle(
    player_drone_count: int,
    player_drone_type: str,
    player_pilot_rank: str,
    methanoid_drone_count: int
) -> Tuple[bool, int, int]:
    """Resolve a battle between player and Methanoid fleets."""
    player_power = calculate_fleet_power(player_drone_count, player_drone_type, player_pilot_rank)
    methanoid_power = calculate_fleet_power(methanoid_drone_count, "IOS", "None")
    
    total_power = player_power + methanoid_power
    player_ratio = player_power / total_power
    
    random_factor = random.uniform(0.9, 1.1)
    adjusted_ratio = player_ratio * random_factor
    
    player_victory = adjusted_ratio > 0.5
    
    if player_victory:
        player_losses = int(methanoid_drone_count * (1 - player_ratio) * random.uniform(0.7, 0.9))
        methanoid_losses = methanoid_drone_count
    else:
        player_losses = player_drone_count
        methanoid_losses = int(player_drone_count * player_ratio * random.uniform(0.7, 0.9))
    
    return player_victory, player_losses, methanoid_losses

def run_simulation(
    player_drone_count: int,
    player_drone_type: str,
    player_pilot_rank: str,
    methanoid_drone_count: int,
    iterations: int = 1000
) -> List[BattleResult]:
    """Run multiple battle simulations and return results."""
    results = []
    for _ in range(iterations):
        victory, player_losses, methanoid_losses = resolve_battle(
            player_drone_count, player_drone_type, player_pilot_rank, methanoid_drone_count
        )
        results.append(BattleResult(
            player_victory=victory,
            player_losses=player_losses,
            methanoid_losses=methanoid_losses,
            player_drone_type=player_drone_type,
            player_pilot_rank=player_pilot_rank,
            player_drone_count=player_drone_count,
            methanoid_drone_count=methanoid_drone_count
        ))
    return results

def analyze_results(results: List[BattleResult]) -> dict:
    """Analyze battle results and return statistics."""
    victories = sum(1 for r in results if r.player_victory)
    win_rate = victories / len(results)
    
    player_losses = [r.player_losses for r in results]
    methanoid_losses = [r.methanoid_losses for r in results]
    
    return {
        "win_rate": win_rate,
        "avg_player_losses": mean(player_losses),
        "std_player_losses": stdev(player_losses) if len(player_losses) > 1 else 0,
        "avg_methanoid_losses": mean(methanoid_losses),
        "std_methanoid_losses": stdev(methanoid_losses) if len(methanoid_losses) > 1 else 0
    }

def format_fleet_info(count: int, type_str: str, rank: str, power: int) -> str:
    """Format fleet information string."""
    rank_str = f" ({rank})" if rank != "None" else ""
    return f"{count} {type_str}{rank_str} (Power: {power})"

def print_header():
    """Print header for results table."""
    headers = [
        "Scenario",
        "Player Fleet",
        "Methanoid Fleet",
        "Win Rate",
        "Player Losses",
        "Methanoid Losses"
    ]
    print(f"{headers[0]:<30} {headers[1]:<35} {headers[2]:<25} {headers[3]:<10} {headers[4]:<20} {headers[5]:<20}")
    print("-" * 140)

def print_result(scenario: str, stats: dict, player_info: tuple, methanoid_count: int):
    """Print formatted battle statistics."""
    player_count, player_type, player_rank = player_info
    player_power = calculate_fleet_power(player_count, player_type, player_rank)
    methanoid_power = calculate_fleet_power(methanoid_count, "IOS", "None")
    
    player_fleet = format_fleet_info(player_count, player_type, player_rank, player_power)
    methanoid_fleet = format_fleet_info(methanoid_count, "IOS", "None", methanoid_power)
    
    print(
        f"{scenario:<30} "
        f"{player_fleet:<35} "
        f"{methanoid_fleet:<25} "
        f"{stats['win_rate']:>8.1%}  "
        f"{stats['avg_player_losses']:>6.1f}±{stats['std_player_losses']:>4.1f}     "
        f"{stats['avg_methanoid_losses']:>6.1f}±{stats['std_methanoid_losses']:>4.1f}"
    )

def main():
    # Test cases
    test_cases = [
        # Equal forces
        (200, "IOS", "None", 200, "Equal IOS"),
        (200, "IOS", "Warlord", 200, "Equal Warlord"),
        (200, "Star", "None", 200, "Equal Star"),
        
        (200, "IOS", "None", 190, "Advantage 10"),
        (200, "IOS", "None", 170, "Advantage 30"),
        (200, "IOS", "None", 150, "Advantage 50"),
        (200, "IOS", "None", 100, "Advantage 100"),
        (200, "IOS", "None", 50, "Advantage 150"),
        (200, "IOS", "None", 1, "Tiny"),
    
        (50, "IOS", "None", 40, "Advantage 10"),
        (50, "IOS", "None", 20, "Advantage 30"),
        (50, "IOS", "None", 1, "Tiny"),

    ]
    
    print("\nDeuteros Battle Simulator")
    print("=" * 140)
    print_header()
    
    for player_count, drone_type, pilot_rank, methanoid_count, scenario in test_cases:
        results = run_simulation(player_count, drone_type, pilot_rank, methanoid_count)
        stats = analyze_results(results)
        print_result(scenario, stats, (player_count, drone_type, pilot_rank), methanoid_count)
    
    print("\nNote: Each scenario simulated 1000 times. Losses shown as mean±std")

if __name__ == "__main__":
    main() 