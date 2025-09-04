def start_chat_ui():
    print("=" * 50)
    print("🤖 Welcome to NeuroBot Lite")
    print("Your emotional assistant for focus, stress, and clarity.")
    print("=" * 50)

    moods = ["Stressed", "Tired", "Focused", "Anxious", "Bored"]
    for i, mood in enumerate(moods, start=1):
        print(f"{i}. {mood}")

    try:
        choice = int(input("\nEnter the number corresponding to your mood: "))
        return moods[choice - 1].lower()
    except (ValueError, IndexError):
        print("⚠️ Invalid input.")
        return None