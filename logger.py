import json
from datetime import datetime

def log_session(mood, suggestion, feedback):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "mood": mood,
        "suggestion": suggestion,
        "feedback": feedback
    }
    try:
        with open("assets/mood_log.json", "r+") as file:
            data = json.load(file)
            data.append(entry)
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open("assets/mood_log.json", "w") as file:
            json.dump([entry], file, indent=4)