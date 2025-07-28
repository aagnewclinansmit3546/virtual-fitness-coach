# Virtual Fitness Coach

This project is a virtual fitness coach application that allows users to log workouts, view workout history, and analyze workout statistics. Users can also export their workout data to a CSV file.

## Features

- **Log New Workouts**: Users can log their workouts with relevant details.
- **View Workout History**: Users can view a history of all logged workouts.
- **View Summary Statistics**: Users can view summary statistics of their workouts, such as total workouts, average duration, etc.
- **Export Data to CSV**: Users can export their workout data to a CSV file for further analysis.
- **Exit the Program**: Users can exit the application gracefully.

## Project Structure

```
virtual-fitness-coach
├── src
│   ├── app.py
│   ├── workouts
│   │   ├── logger.py
│   │   ├── history.py
│   │   └── summary.py
│   ├── export
│   │   └── csv_exporter.py
│   └── utils
│       └── menu.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd virtual-fitness-coach
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

## Usage Guidelines

- Follow the on-screen menu to log workouts, view history, and access summary statistics.
- Use the export feature to save your workout data in CSV format.
- To exit the application, select the exit option from the menu.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
