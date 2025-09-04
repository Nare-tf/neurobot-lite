from cli_ui import start_chat_ui
from ai_simulator import ai_response
from feedback import get_feedback
from logger import log_session

def run_bot():
    mood = start_chat_ui()
    if not mood:
        return

    suggestion = ai_response(mood)
    print(f"\nNeuroBot: {suggestion}")

    feedback = get_feedback()
    log_session(mood, suggestion, feedback)

    print("\nNeuroBot: Got it. Keep going—you’ve got this.")

if __name__ == "__main__":
    run_bot()