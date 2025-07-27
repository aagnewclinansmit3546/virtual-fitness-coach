# Virtual Fitness Coach Application

from workouts.logger import Logger
from workouts.history import History
from workouts.summary import Summary
from export.csv_exporter import CSVExporter
from utils.menu import Menu

def main():
    logger = Logger()
    history = History()
    summary = Summary()
    csv_exporter = CSVExporter()
    menu = Menu(logger, history, summary, csv_exporter)

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
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()