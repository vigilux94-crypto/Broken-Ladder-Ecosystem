import sys
import os
import random

# Ensure Python can see your modules
sys.path.append(os.path.join(os.getcwd(), "backend-eris"))
sys.path.append(os.path.join(os.getcwd(), "sober-economy"))
sys.path.append(os.path.join(os.getcwd(), "compliance-ohio"))

from risk_engine import ERISCore
from rewards import SoberEconomy
from billing_logic import OhioMedicaidBilling

def run_monthly_impact_report(user_id):
    eris = ERISCore()
    economy = SoberEconomy()
    billing = OhioMedicaidBilling()
    
    monthly_statuses = []
    total_management_mins = 0
    
    print(f"--- Monthly Impact Report for {user_id} ---")
    
    # Simulate 30 days of ecosystem interaction
    for day in range(1, 31):
        # Most days are compliant (GREEN), some are high-stress (YELLOW)
        daily_output = ["GREEN"] * 24
        if random.random() < 0.15:
            daily_output[random.randint(0, 23)] = "YELLOW"
            total_management_mins += 5 # CDCA spends 5 mins reviewing a yellow alert
            
        monthly_statuses.extend(daily_output)

    # 1. Calculate Rewards
    # (Simplified for the 30-day view)
    total_coins = 0
    for i in range(0, len(monthly_statuses), 24):
        total_coins += economy.calculate_daily_reward(monthly_statuses[i:i+24])
        
    # 2. Calculate Billing
    monitoring_days = 30 
    billable_items = billing.determine_billing(monitoring_days, total_management_mins)
    
    # --- Final Output ---
    print(f"Total SOBER Coins Earned: {total_coins}")
    print(f"Clinical Review Time: {total_management_mins} minutes")
    print("\nPROPOSED BILLING:")
    grand_total = 0
    for item in billable_items:
        print(f"- {item['code']}: {item['desc']} (${item['amt']:.2f})")
        grand_total += item['amt']
    
    print(f"\nMONTHLY REVENUE GENERATED: ${grand_total:.2f}")
    print("-------------------------------------------")

if __name__ == "__main__":
    run_monthly_impact_report("TobyP_001")
