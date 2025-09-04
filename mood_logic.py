def get_suggestion(mood):
    suggestions = {
        "stressed": ["Try a breathing exercise.", "Take a short walk."],
        "tired": ["Hydrate and stretch.", "Take a power nap."],
        "focused": ["Set a timer and keep going!", "You're in the zone."],
        "anxious": ["Break tasks into steps.", "Write down your thoughts."],
        "bored": ["Switch subjects.", "Try a creative break."]
    }
    return suggestions.get(mood, ["I'm not sure how to help with that yet."])