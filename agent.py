# 🏏 Batting Agent
def batting_agent(player):
    sr = player.strike_rate()
    runs = player.runs
    wickets = player.wickets   # using as match context (pressure)

    # 🔥 High impact innings
    if runs >= 50 and sr >= 150:
        if wickets >= 7:
            return "🔥 Match-saving knock under pressure"
        else:
            return "🔥 Dominant batting performance"

    # 👍 Good but not match-defining
    elif runs >= 30 and sr >= 120:
        return "👍 Solid batting contribution"

    # ⚠️ Quick but low impact
    elif runs < 30 and sr >= 140:
        return "⚠️ Quick runs but limited impact"

    # ⚠️ Slow innings
    elif sr < 100:
        return "⚠️ Slow scoring rate — needs improvement"

    # ❌ Poor
    else:
        return "❌ Weak batting performance"


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