class Logger:
    def __init__(self):
        self.workouts = []

    def log_workout(self, workout_type, duration, date):
        if self.validate_input(workout_type, duration, date):
            workout = {
                'type': workout_type,
                'duration': duration,
                'date': date
            }
            self.workouts.append(workout)
            return True
        return False

    def validate_input(self, workout_type, duration, date):
        if not isinstance(workout_type, str) or not workout_type:
            return False
        if not isinstance(duration, (int, float)) or duration <= 0:
            return False
        if not isinstance(date, str) or not date:
            return False
        return True

    def get_workouts(self):
        return self.workouts