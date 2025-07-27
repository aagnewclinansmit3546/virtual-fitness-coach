class CSVExporter:
    def __init__(self, filename):
        self.filename = filename

    def export_data(self, workout_data):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Workout Type', 'Duration', 'Calories Burned'])  # Header row
            for workout in workout_data:
                writer.writerow([workout['date'], workout['type'], workout['duration'], workout['calories']])

    def save_workout_data(self, workout_data):
        self.export_data(workout_data)