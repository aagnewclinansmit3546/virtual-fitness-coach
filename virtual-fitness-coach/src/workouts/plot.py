import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt

class Plot:
    def __init__(self, csv_filename='workouts.csv'):
        self.csv_filename = csv_filename

    def load_data(self):
        if not os.path.isfile(self.csv_filename):
            print("❌ No workout data found.")
            return {}

        calories_per_day = defaultdict(float)

        with open(self.csv_filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    date = row['Date']
                    calories = float(row['Calories'])
                    calories_per_day[date] += calories
                except (KeyError, ValueError):
                    continue  # Skip bad rows

        return dict(calories_per_day)

    def plot_calories_per_day(self):
        data = self.load_data()
        if not data:
            print("❌ Nothing to plot.")
            return

        dates = sorted(data.keys())
        calories = [data[date] for date in dates]

        plt.figure(figsize=(10, 5))
        plt.plot(dates, calories, marker='o', linestyle='-', color='orange')
        plt.title("Calories Burned per Day")
        plt.xlabel("Date")
        plt.ylabel("Calories Burned")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()