import csv
import os

class CSVExporter:
    def __init__(self, output_filename='workouts.csv'):
        self.output_filename = output_filename

    def export_to_csv(self):
        input_filename = input("Enter the path to the sample CSV file to import: ").strip()

        if not os.path.isfile(input_filename):
            print(f"❌ Input file '{input_filename}' not found.")
            return

        try:
            with open(input_filename, mode='r') as infile, \
                 open(self.output_filename, mode='w', newline='') as outfile:

                reader = csv.DictReader(infile)
                fieldnames = ['Workout Type', 'Duration', 'Date', 'Calories']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                count = 0
                for row in reader:
                    try:
                        writer.writerow({
                            'Workout Type': row['Workout Type'],
                            'Duration': float(row['Duration']),
                            'Date': row['Date'],
                            'Calories': float(row['Calories'])
                        })
                        count += 1
                    except (KeyError, ValueError):
                        print("⚠️ Skipping invalid row:", row)
                        continue

            print(f"✅ Imported {count} workouts from '{input_filename}' into '{self.output_filename}'.")
        except Exception as e:
            print(f"❌ Failed to export: {e}")
