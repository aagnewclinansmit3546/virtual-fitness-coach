import csv
import os

class Summary:
    def __init__(self, csv_filename='workouts.csv'):
        self.csv_filename = csv_filename

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

    def total_workouts(self, workouts):
        return len(workouts)

    def average_duration(self, workouts):
        if not workouts:
            return 0
        total_duration = sum(workout['duration'] for workout in workouts)
        return total_duration / len(workouts)

    def total_calories(self, workouts):
        return sum(workout['calories'] for workout in workouts)

    def average_calories(self, workouts):
        if not workouts:
            return 0
        return self.total_calories(workouts) / len(workouts)

    def summary_statistics(self):
        workouts = self.load_workouts()
        stats = {
            'Total Workouts': self.total_workouts(workouts),
            'Average Duration (min)': round(self.average_duration(workouts), 2),
            'Total Calories Burned': round(self.total_calories(workouts), 2),
            'Average Calories Burned': round(self.average_calories(workouts), 2)
        }

        return stats

    def display_summary(self):
        stats = self.summary_statistics()

        if not stats['Total Workouts']:
            print("No workout data available.")
            return

        print("\nWorkout Summary:")
        for key, value in stats.items():
            print(f"- {key}: {value}")