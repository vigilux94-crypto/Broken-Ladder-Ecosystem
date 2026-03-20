class OhioMedicaidBilling:
    def __init__(self):
        # 2026 Ohio Medicaid National Averages (Approximated)
        self.rates = {
            "99453": 21.71,  # Initial Setup
            "99445": 47.00,  # 2-15 days monitoring (New 2026 Code)
            "99454": 47.00,  # 16-30 days monitoring
            "99470": 26.00   # First 10 mins of management (New 2026 Code)
        }

    def determine_billing(self, monitoring_days, management_minutes=0):
        billable_items = []
        
        # Device Supply & Data Transmission
        if 2 <= monitoring_days <= 15:
            billable_items.append({"code": "99445", "desc": "Device Supply (Short-term)", "amt": self.rates["99445"]})
        elif monitoring_days >= 16:
            billable_items.append({"code": "99454", "desc": "Device Supply (Full-month)", "amt": self.rates["99454"]})
            
        # Clinical Management Time
        if 10 <= management_minutes < 20:
            billable_items.append({"code": "99470", "desc": "Clinical Mgmt (10-19 min)", "amt": self.rates["99470"]})
        elif management_minutes >= 20:
            # Note: 99457 is used for 20+ minutes
            billable_items.append({"code": "99457", "desc": "Clinical Mgmt (20+ min)", "amt": 52.00})
            
        return billable_items

if __name__ == "__main__":
    billing = OhioMedicaidBilling()
    # Using your 30-day simulation data
    results = billing.determine_billing(monitoring_days=30, management_minutes=15)
    
    print("--- Ohio Medicaid 2026 Billing Preview ---")
    total = 0
    for item in results:
        print(f"Code: {item['code']} | {item['desc']:<25} | ${item['amt']:.2f}")
        total += item['amt']
    print(f"Total Potential Reimbursement: ${total:.2f}")
