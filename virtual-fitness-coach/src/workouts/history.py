import csv
import os

class History:
    def __init__(self, csv_filename='workouts.csv'):
        self.csv_filename = csv_filename
        self.workouts = self.load_workouts()

    def load_workouts(self):
        if not os.path.isfile(self.csv_filename):
            return []

        workouts = []
        with open(self.csv_filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    workouts.append({
                        'type': row['Workout Type'],
                        'duration': float(row['Duration']),
                        'date': row['Date'],
                        'calories': float(row['Calories'])
                    })
                except (KeyError, ValueError):
                    continue
        return workouts

    def add_workout(self, workout):
        self.workouts.append(workout)

    def get_workout_history(self):
        return self.workouts

    def display_history(self):
        self.workouts = self.load_workouts()

        if not self.workouts:
            print("No workouts logged yet.")
            return

        print("Workout History:")
        for index, workout in enumerate(self.workouts, start=1):
            print(
                f"{index}. Type: {workout['type']}, "
                f"Duration: {workout['duration']} min, "
                f"Date: {workout['date']}, "
                f"Calories: {workout['calories']} kcal"
            )