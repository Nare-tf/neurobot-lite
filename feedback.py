def get_feedback():
    response = input("Did that help a little? (yes/no): ").strip().lower()
    return response in ["yes", "y"]