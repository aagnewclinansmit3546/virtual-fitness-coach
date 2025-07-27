class History:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def get_workout_history(self):
        return self.workouts

    def display_history(self):
        if not self.workouts:
            return "No workouts logged yet."
        
        history_str = "Workout History:\n"
        for index, workout in enumerate(self.workouts, start=1):
            history_str += f"{index}. {workout}\n"
        return history_str.strip()