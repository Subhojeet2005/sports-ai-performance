def analyze(player):
    score = player.score()

    return {
        "score": score,
        "analysis": "App is working ✅",
        "summary": "Basic test success",
        "suggestions": ["System running fine"]
    }