import questionary

# Ask the player a question with multiple choices
choice = questionary.select(
    "What would you like to do?",
    choices=["Explore the city", "Visit the tavern", "Train at the barracks", "Rest at the inn"]
).ask()

# Display the player's choice
print(f"You chose to: {choice}")
