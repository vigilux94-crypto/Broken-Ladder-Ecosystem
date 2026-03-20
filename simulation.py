import sys
import os
import random

# Tell Python to look in the subfolders
sys.path.append(os.path.join(os.getcwd(), "backend-eris"))
sys.path.append(os.path.join(os.getcwd(), "sober-economy"))

from risk_engine import ERISCore
from rewards import SoberEconomy

def run_30_day_test():
    eris = ERISCore()
    economy = SoberEconomy()
    total_coins = 0
    
    print(f"{'Day':<5} | {'Status':<10} | {'Coins':<10}")
    print("-" * 30)

    for day in range(1, 31):
        daily_statuses = ["GREEN"] * 24
        # Randomly inject a stress event (YELLOW)
        if random.random() < 0.2:
            daily_statuses[random.randint(0, 23)] = "YELLOW"
            
        coins = economy.calculate_daily_reward(daily_statuses)
        total_coins += coins
        status = "YELLOW" if "YELLOW" in daily_statuses else "GREEN"
        print(f"{day:<5} | {status:<10} | {coins:<10}")

    print("-" * 30)
    print(f"30-Day Total: {total_coins} SOBER Coins")

if __name__ == "__main__":
    run_30_day_test()
