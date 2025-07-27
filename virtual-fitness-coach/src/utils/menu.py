class Menu:
    def __init__(self):
        self.options = {
            '1': 'Log New Workout',
            '2': 'View Workout History',
            '3': 'View Summary Statistics',
            '4': 'Export Data to CSV',
            '5': 'Exit'
        }

    def display_menu(self):
        print("\n--- Virtual Fitness Coach Menu ---")
        for key, value in self.options.items():
            print(f"{key}. {value}")
        print("-----------------------------------")

    def get_user_choice(self):
        choice = input("Please select an option: ")
        return choice.strip()

    def handle_choice(self, choice):
        if choice in self.options:
            return choice
        else:
            print("Invalid choice. Please try again.")
            return None