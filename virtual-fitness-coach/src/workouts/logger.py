import csv
import os

class Logger:
    def __init__(self, csv_filename='workouts.csv'):
        self.workouts = []
        self.csv_filename = csv_filename

    def log_workout(self):
        workout_type = input("Enter workout type (e.g., cardio, strength): ").strip()
        if not self.validate_workout_type(workout_type):
            print("❌ Invalid workout type.")
            return False

        try:
            duration = float(input("Enter duration in minutes: ").strip())
            if not self.validate_duration(duration):
                print("❌ Duration must be a positive number.")
                return False
        except ValueError:
            print("❌ Invalid input. Duration must be a number.")
            return False

        date = input("Enter date (e.g., 2025-07-27): ").strip()
        if not self.validate_date(date):
            print("❌ Invalid date.")
            return False

        try:
            calories = float(input("Enter calories burned: ").strip())
            if not self.validate_calories(calories):
                print("❌ Calories must be a positive number.")
                return False
        except ValueError:
            print("❌ Invalid input. Calories must be a number.")
            return False

        workout = {
            'type': workout_type,
            'duration': duration,
            'date': date,
            'calories': calories
        }

        self.workouts.append(workout)
        self.append_to_csv(workout)
        print("✅ Workout logged and saved.")
        return True

    def append_to_csv(self, workout):
        file_exists = os.path.isfile(self.csv_filename)
        with open(self.csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Workout Type', 'Duration', 'Date', 'Calories'])  # header
            writer.writerow([workout['type'], workout['duration'], workout['date'], workout['calories']])

    def validate_workout_type(self, workout_type):
        return isinstance(workout_type, str) and len(workout_type.strip()) > 0

    def validate_duration(self, duration):
        return isinstance(duration, (int, float)) and duration > 0

    def validate_date(self, date):
        return isinstance(date, str) and len(date.strip()) > 0

    def validate_calories(self, calories):
        return isinstance(calories, (int, float)) and calories > 0

    def get_workouts(self):
        return self.workouts