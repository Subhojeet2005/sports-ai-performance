class PlayerPerformance:
    def __init__(self, runs, balls, wickets, catches):
        self.runs = runs
        self.balls = balls
        self.wickets = wickets
        self.catches = catches

    def strike_rate(self):
        return (self.runs / self.balls) * 100 if self.balls else 0

    def score(self):
        return round(
            self.runs * 0.5 +
            self.strike_rate() * 0.3 +
            self.wickets * 20 +
            self.catches * 10,
            2
        )