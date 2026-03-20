import datetime

class ERISCore:
    def __init__(self):
        self.thresholds = {
            "stress_high": 75,
            "heart_rate_max": 110,
            "alcohol_limit": 0.02
        }

    def analyze_biometrics(self, user_id, ppg_hr, gsr_stress, alcohol_level):
        status = "GREEN"
        alerts = []
        if alcohol_level > self.thresholds["alcohol_limit"]:
            status = "RED"
            alerts.append("ALCOHOL_DETECTED")
        elif gsr_stress > self.thresholds["stress_high"] or ppg_hr > self.thresholds["heart_rate_max"]:
            status = "YELLOW"
            alerts.append("HIGH_STRESS_ANOMALY")
        return {
            "timestamp": datetime.datetime.now().isoformat(),
            "user_id": user_id,
            "status": status,
            "alerts": alerts
        }

if __name__ == "__main__":
    engine = ERISCore()
    result = engine.analyze_biometrics("TobyP_001", 115, 80, 0.00)
    print(f"ERIS Status: {result['status']} | Alerts: {result['alerts']}")
