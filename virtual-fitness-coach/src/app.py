# Virtual Fitness Coach Application

from workouts.logger import Logger
from workouts.history import History
from workouts.summary import Summary
from workouts.plot import Plot
from export.csv_exporter import CSVExporter
from utils.menu import Menu

FILENAME = "workouts.csv"

def main():
    logger = Logger()
    history = History()
    summary = Summary()
    plot = Plot()
    csv_exporter = CSVExporter(FILENAME)
    menu = Menu()

    while True:
        choice = menu.display_menu()
        if choice == '1':
            logger.log_workout()
        elif choice == '2':
            history.display_history()
        elif choice == '3':
            summary.display_summary()
        elif choice == '4':
            csv_exporter.export_to_csv()
        elif choice == '5':
            plot.plot_calories_per_day()
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()