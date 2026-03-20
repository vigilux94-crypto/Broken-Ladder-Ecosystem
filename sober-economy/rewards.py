class SoberEconomy:
    def __init__(self):
        # 10 points per hour in GREEN status
        self.points_per_compliant_hour = 10
        # 1.5x multiplier for a full 24-hour streak
        self.bonus_multiplier = 1.5 

    def calculate_daily_reward(self, hourly_statuses):
        """
        hourly_statuses: A list of 24 strings (e.g., "GREEN", "YELLOW", "RED")
        """
        total_points = 0
        streak = 0
        
        for status in hourly_statuses:
            if status == "GREEN":
                total_points += self.points_per_compliant_hour
                streak += 1
            else:
                # Streak resets on Yellow (Warning) or Red (Relapse/Risk)
                streak = 0 
                
        if streak >= 24:
            total_points = int(total_points * self.bonus_multiplier)
            
        return total_points

if __name__ == "__main__":
    economy = SoberEconomy()
    # Test Case: A perfect compliant day
    perfect_day = ["GREEN"] * 24
    reward = economy.calculate_daily_reward(perfect_day)
    print(f"Daily SOBER Coin Earnings: {reward} coins")
    
    # Test Case: A day with a stress spike (YELLOW) at hour 12
    rough_day = ["GREEN"] * 12 + ["YELLOW"] + ["GREEN"] * 11
    rough_reward = economy.calculate_daily_reward(rough_day)
    print(f"Earnings with stress spike: {rough_reward} coins")
