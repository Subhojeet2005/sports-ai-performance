def analyze(player):
    score = player.score()

    if score > 150:
        analysis = "Excellent performance"
    elif score > 100:
        analysis = "Good performance"
    elif score > 60:
        analysis = "Average performance"
    else:
        analysis = "Poor performance"

    suggestions = []

    if player.strike_rate() < 120:
        suggestions.append("Improve strike rate")

    if player.wickets == 0:
        suggestions.append("Work on bowling")

    if player.catches == 0:
        suggestions.append("Improve fielding")

    return score, analysis, suggestions