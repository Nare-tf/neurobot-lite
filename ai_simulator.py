import random
from mood_logic import get_suggestion

def ai_response(mood):
    responses = get_suggestion(mood)
    return random.choice(responses)