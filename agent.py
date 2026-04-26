def analyze(player):
    score = player.score()
    strike_rate = player.strike_rate()

    # 🎯 Performance level
    if score >= 150:
        level = "🔥 Excellent"
    elif score >= 100:
        level = "👍 Good"
    elif score >= 60:
        level = "⚠️ Average"
    else:
        level = "❌ Poor"

    analysis = f"{level} performance with score {score}"

    # 💡 Suggestions
    suggestions = []

    # Batting
    if strike_rate < 100:
        suggestions.append("Increase strike rate — play more attacking shots")
    elif strike_rate > 150:
        suggestions.append("Outstanding strike rate — keep dominating")

    # Bowling
    if player.wickets == 0:
        suggestions.append("Improve bowling accuracy and variation")
    elif player.wickets >= 3:
        suggestions.append("Excellent bowling performance")

    # Fielding
    if player.catches == 0:
        suggestions.append("Work on fielding reflexes")
    else:
        suggestions.append("Good fielding contribution")

    # 🧠 Summary
    if score >= 120 and player.wickets >= 1:
        summary = "Strong all-round performance 💪"
    elif score < 60:
        summary = "Needs major improvement"
    else:
        summary = "Decent performance with scope to improve"

    return {
        "score": score,
        "analysis": analysis,
        "summary": summary,
        "suggestions": suggestions
    }