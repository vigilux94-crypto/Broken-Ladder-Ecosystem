import sys, os, random
sys.path.append(os.path.join(os.getcwd(), "backend-eris"))
sys.path.append(os.path.join(os.getcwd(), "sober-economy"))
sys.path.append(os.path.join(os.getcwd(), "compliance-ohio"))
from billing_logic import OhioMedicaidBilling

def run_impact():
    billing = OhioMedicaidBilling()
    # Simulation: 30 days data, 40m review, 2 hours Peer Support
    billable = billing.determine_billing(days=30, review_mins=40, peer_hrs=2)
    print("\n--- 🛡️ VIGIL BOS: 2026 REVENUE REPORT ---")
    total = 0
    for i in billable:
        amt = i['amt']
        print(f"{i['code']:<6} | ${amt:>7.2f}")
        total += amt
    print(f"---------------------------------------")
    print(f"TOTAL REVENUE / PATIENT: ${total:.2f}")

if __name__ == "__main__": run_impact()
