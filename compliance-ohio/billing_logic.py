class OhioMedicaidBilling:
    def __init__(self):
        # 2026 Finalized Rates (Rule 5160-1-18)
        self.rates = {
            "99453": 21.71, "99445": 52.11, "99454": 52.11,
            "99470": 26.05, "99457": 51.77, "99458": 41.42,
            "99490": 66.13, "H0038": 15.51 # Per 15-min unit
        }

    def determine_billing(self, days, review_mins, peer_hrs):
        billable = []
        # Monitoring Supply
        if 2 <= days <= 15: billable.append({"code":"99445", "amt":self.rates["99445"]})
        elif days >= 16: billable.append({"code":"99454", "amt":self.rates["99454"]})
        # Clinical Management
        if 10 <= review_mins < 20: billable.append({"code":"99470", "amt":self.rates["99470"]})
        elif review_mins >= 20:
            billable.append({"code":"99457", "amt":self.rates["99457"]})
            if review_mins >= 40: billable.append({"code":"99458", "amt":self.rates["99458"]})
        # Care Coordination & Peer Support
        billable.append({"code":"99490", "amt":self.rates["99490"]})
        peer_units = int(peer_hrs * 4)
        if peer_units > 0: billable.append({"code":"H0038", "units":peer_units, "amt":self.rates["H0038"] * peer_units})
        return billable
