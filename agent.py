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

    # 📊 Detailed analysis
    analysis = f"{level} performance with score {score}"

    # 💡 Suggestions engine (agent-like behavior)
    suggestions = []

    # Batting analysis
    if strike_rate < 100:
        suggestions.append("Increase strike rate — play more attacking shots")
    elif strike_rate > 150:
        suggestions.append("Great strike rate — maintain aggressive intent")

    # Bowling analysis
    if player.wickets == 0:
        suggestions.append("Focus on bowling accuracy and variations")
    elif player.wickets >= 3:
        suggestions.append("Excellent bowling impact")

    # Fielding analysis
    if player.catches == 0:
        suggestions.append("Improve fielding drills and reflexes")
    else:
        suggestions.append("Good fielding contribution")

    # 🧠 Final agent decision (summary insight)
    if score >= 120 and player.wickets >= 1:
        summary = "Strong all-round performance 💪"
    elif score < 60:
        summary = "Needs improvement in multiple areas"
    else:
        summary = "Decent performance with room to improve"

    return {
        "score": score,
        "analysis": analysis,
        "summary": summary,
        "suggestions": suggestions
    }