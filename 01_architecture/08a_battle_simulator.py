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
    rounds: List[dict]  # Store round-by-round information

def calculate_fleet_power(drone_count: int, drone_type: str, pilot_rank: str) -> int:
    """Calculate total fleet power based on drone count, type and pilot rank."""
    if drone_type == "IOS":
        base_power = 7
        if pilot_rank == "Warlord":
            base_power += 3
    else:  # Star Drone
        base_power = 10
    return drone_count * base_power

def calculate_round_losses(attacker_power: int, defender_power: int, luck_factor: float) -> int:
    """Calculate losses for a single round of combat."""
    # Add more chaos with additional randomness
    chaos_factor = random.uniform(0.5, 1.5)  # High variance chaos factor
    
    # Power ratio with more randomness
    power_ratio = attacker_power / (attacker_power + defender_power)
    adjusted_ratio = power_ratio * luck_factor * chaos_factor
    
    # More random base losses
    random_intensity = random.uniform(0.02, 0.06)  # Varies the intensity of combat
    base_losses = int(defender_power * random_intensity * (attacker_power / defender_power))
    
    # Chance for critical hit
    if random.random() < 0.1:  # 10% chance for critical hit
        base_losses = int(base_losses * random.uniform(1.5, 2.5))
    
    return max(1, int(base_losses * adjusted_ratio))

def resolve_battle(
    player_drone_count: int,
    player_drone_type: str,
    player_pilot_rank: str,
    methanoid_drone_count: int
) -> Tuple[bool, int, int, List[dict]]:
    """Resolve a battle between player and Methanoid fleets using rounds."""
    current_player_count = player_drone_count
    current_methanoid_count = methanoid_drone_count
    rounds = []
    player_luck = 1.0
    round_number = 0
    
    # Chance for immediate advantage to either side
    battle_momentum = random.uniform(0.9, 1.1)
    player_momentum = battle_momentum
    methanoid_momentum = 2 - battle_momentum
    
    while current_player_count > 0 and current_methanoid_count > 0:
        round_number += 1
        
        # Calculate current powers
        player_power = calculate_fleet_power(current_player_count, player_drone_type, player_pilot_rank)
        methanoid_power = calculate_fleet_power(current_methanoid_count, "IOS", "None")
        
        # Update luck factor with wider swings
        player_luck = random.uniform(0.7, 1.3)
        
        # Update momentum (can shift dramatically)
        if random.random() < 0.15:  # 15% chance for momentum shift
            momentum_shift = random.uniform(-0.2, 0.2)
            player_momentum = max(0.6, min(1.4, player_momentum + momentum_shift))
            methanoid_momentum = 2 - player_momentum
        
        # Calculate round losses with increased chaos
        methanoid_round_losses = calculate_round_losses(
            player_power, 
            methanoid_power, 
            player_luck * player_momentum
        )
        player_round_losses = calculate_round_losses(
            methanoid_power, 
            player_power, 
            (2 - player_luck) * methanoid_momentum
        )
        
        # Random event: overwhelming assault (rare)
        if random.random() < 0.05:  # 5% chance
            if random.random()>=0.5:
                methanoid_round_losses = int(methanoid_round_losses * random.uniform(2.0, 3.0))
                print_event = "Player's fleet executes a brilliant maneuver!"
            else:
                player_round_losses = int(player_round_losses * random.uniform(2.0, 3.0))
                print_event = "Methanoids launch a devastating attack!"
        else:
            print_event = None
        
        # Apply losses
        current_methanoid_count = max(0, current_methanoid_count - methanoid_round_losses)
        current_player_count = max(0, current_player_count - player_round_losses)
        
        # Record round results
        rounds.append({
            "round": round_number,
            "player_count": current_player_count,
            "methanoid_count": current_methanoid_count,
            "player_losses": player_round_losses,
            "methanoid_losses": methanoid_round_losses,
            "luck_factor": player_luck,
            "player_power": player_power,
            "methanoid_power": methanoid_power,
            "player_momentum": player_momentum,
            "event": print_event
        })
    
    player_victory = current_player_count > 0
    total_player_losses = player_drone_count - current_player_count
    total_methanoid_losses = methanoid_drone_count - current_methanoid_count
    
    return player_victory, total_player_losses, total_methanoid_losses, rounds

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
        victory, player_losses, methanoid_losses, rounds = resolve_battle(
            player_drone_count, player_drone_type, player_pilot_rank, methanoid_drone_count
        )
        results.append(BattleResult(
            player_victory=victory,
            player_losses=player_losses,
            methanoid_losses=methanoid_losses,
            player_drone_type=player_drone_type,
            player_pilot_rank=player_pilot_rank,
            player_drone_count=player_drone_count,
            methanoid_drone_count=methanoid_drone_count,
            rounds=rounds
        ))
    return results

def analyze_results(results: List[BattleResult]) -> dict:
    """Analyze battle results and return statistics."""
    victories = sum(1 for r in results if r.player_victory)
    win_rate = victories / len(results)
    
    player_losses = [r.player_losses for r in results]
    methanoid_losses = [r.methanoid_losses for r in results]
    rounds_count = [len(r.rounds) for r in results]
    
    return {
        "win_rate": win_rate,
        "avg_player_losses": mean(player_losses),
        "std_player_losses": stdev(player_losses) if len(player_losses) > 1 else 0,
        "avg_methanoid_losses": mean(methanoid_losses),
        "std_methanoid_losses": stdev(methanoid_losses) if len(methanoid_losses) > 1 else 0,
        "avg_rounds": mean(rounds_count),
        "std_rounds": stdev(rounds_count) if len(rounds_count) > 1 else 0
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
        "P.Power",
        "Methanoid Fleet",
        "M.Power",
        "Win Rate",
        "Rounds",
        "P.Losses",
        "M.Losses"
    ]
    print(f"{headers[0]:<30} {headers[1]:<20} {headers[2]:<8} {headers[3]:<20} {headers[4]:<8} {headers[5]:<8} {headers[6]:<8} {headers[7]:<12} {headers[8]:<12}")
    print("-" * 140)

def print_result(scenario: str, stats: dict, player_info: tuple, methanoid_count: int):
    """Print formatted battle statistics."""
    player_count, player_type, player_rank = player_info
    player_power = calculate_fleet_power(player_count, player_type, player_rank)
    methanoid_power = calculate_fleet_power(methanoid_count, "IOS", "None")
    
    player_fleet = f"{player_count} {player_type}"
    if player_rank != "None":
        player_fleet += f" ({player_rank})"
    methanoid_fleet = f"{methanoid_count} IOS"
    
    print(
        f"{scenario:<30} "
        f"{player_fleet:<20} "
        f"{player_power:<8} "
        f"{methanoid_fleet:<20} "
        f"{methanoid_power:<8} "
        f"{stats['win_rate']:>7.1%} "
        f"{stats['avg_rounds']:>7.1f} "
        f"{stats['avg_player_losses']:>6.1f}±{stats['std_player_losses']:>4.1f} "
        f"{stats['avg_methanoid_losses']:>6.1f}±{stats['std_methanoid_losses']:>4.1f}"
    )

def print_detailed_battle(result: BattleResult):
    """Print detailed round-by-round battle information."""
    print("\nDetailed Battle Report")
    print("=" * 120)
    print(f"Initial forces: {result.player_drone_count} {result.player_drone_type} vs {result.methanoid_drone_count} Methanoid IOS")
    print("-" * 120)
    print(f"{'Round':<6} {'Player':<8} {'P.Power':<8} {'Methanoid':<8} {'M.Power':<8} {'P.Losses':<8} {'M.Losses':<8} {'Luck':<6} {'Momentum':<8} {'Event'}")
    print("-" * 120)
    
    for round_data in result.rounds:
        event_text = round_data.get("event", "")
        print(
            f"{round_data['round']:<6} "
            f"{round_data['player_count']:<8} "
            f"{round_data['player_power']:<8} "
            f"{round_data['methanoid_count']:<8} "
            f"{round_data['methanoid_power']:<8} "
            f"{round_data['player_losses']:<8} "
            f"{round_data['methanoid_losses']:<8} "
            f"{round_data['luck_factor']:.2f} "
            f"{round_data.get('player_momentum', 1.0):.2f}     "
            f"{event_text or ''}"
        )
    
    print("-" * 120)
    print(f"Battle outcome: {'Victory' if result.player_victory else 'Defeat'}")
    print(f"Total rounds: {len(result.rounds)}")
    print(f"Final forces - Player: {result.rounds[-1]['player_count']}, Methanoid: {result.rounds[-1]['methanoid_count']}")

def main():
    # Test cases
    test_cases = [
        # Equal forces
        (200, "IOS", "None", 200, "Equal IOS"),
        (200, "IOS", "Warlord", 200, "Equal Warlord"),
        (200, "Star", "None", 200, "Equal Star"),
        
        # Player advantage
        (200, "IOS", "None", 190, "Advantage 10"),
        (200, "IOS", "None", 170, "Advantage 30"),
        (200, "IOS", "None", 150, "Advantage 50"),
        (200, "IOS", "None", 100, "Advantage 100"),
        (200, "IOS", "None", 50, "Advantage 150"),
        (200, "IOS", "None", 1, "Tiny"),
    
        (50, "IOS", "None", 40, "Advantage 10"),
        (50, "IOS", "None", 20, "Advantage 30"),
        (50, "IOS", "None", 1, "Tiny"),

        # Methanoid advantage
        (190, "IOS", "None", 200, "M Advantage 10"),
        (170, "IOS", "None", 200, "M Advantage 30"),
        (150, "IOS", "None", 200, "M Advantage 50"),
        (100, "IOS", "None", 200, "M Advantage 100"),
        (50, "IOS", "None", 200, "M Advantage 150"),
        (1, "IOS", "None", 200, "M Tiny"),

        (40, "IOS", "None", 50, "M Advantage 10"),
        (20, "IOS", "None", 50, "M Advantage 30"),
        (1, "IOS", "None", 50, "M Tiny"),
    ]
    
    print("\nDeuteros Battle Simulator")
    print("=" * 152)
    print_header()
    
    for player_count, drone_type, pilot_rank, methanoid_count, scenario in test_cases:
        results = run_simulation(player_count, drone_type, pilot_rank, methanoid_count)
        stats = analyze_results(results)
        print_result(scenario, stats, (player_count, drone_type, pilot_rank), methanoid_count)
    
    print("\nNote: Each scenario simulated 1000 times. Stats shown as mean±std")
    
    # Print a detailed example battle
    print("\nExample Detailed Battle:")
    example_result = run_simulation(100, "IOS", "None", 100, iterations=1)[0]
    print_detailed_battle(example_result)

if __name__ == "__main__":
    main()