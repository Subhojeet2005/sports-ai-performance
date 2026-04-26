# 🏏 Batting Agent
def batting_agent(player):
    sr = player.strike_rate()

    if player.runs > 50 and sr > 140:
        return "🔥 Excellent batting performance"
    elif player.runs > 30:
        return "👍 Good batting contribution"
    else:
        return "⚠️ Batting needs improvement"


# 🎯 Bowling Agent
def bowling_agent(player):
    if player.wickets >= 3:
        return "🔥 Outstanding bowling spell"
    elif player.wickets >= 1:
        return "👍 Decent bowling effort"
    else:
        return "⚠️ No bowling impact"


# 🧤 Fielding Agent
def fielding_agent(player):
    if player.catches >= 2:
        return "🔥 Excellent fielding"
    elif player.catches == 1:
        return "👍 Good fielding contribution"
    else:
        return "⚠️ Fielding needs improvement"


# 🧠 Final Decision Agent
def analyze(player):
    score = player.score()

    bat = batting_agent(player)
    bowl = bowling_agent(player)
    field = fielding_agent(player)

    # 🧠 Combine insights
    suggestions = []

    if "needs improvement" in bat.lower():
        suggestions.append("Work on batting technique and shot selection")

    if "no bowling impact" in bowl.lower():
        suggestions.append("Improve bowling accuracy and variation")

    if "needs improvement" in field.lower():
        suggestions.append("Practice fielding drills")

    summary = f"{bat} | {bowl} | {field}"

    return {
        "score": score,
        "analysis": summary,
        "summary": "Multi-agent analysis complete 🤖",
        "suggestions": suggestions if suggestions else ["All areas performing well 💯"]
    }