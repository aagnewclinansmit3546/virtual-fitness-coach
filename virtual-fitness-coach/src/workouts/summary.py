class Summary:
    def __init__(self, workouts):
        self.workouts = workouts

    def total_workouts(self):
        return len(self.workouts)

    def average_duration(self):
        if not self.workouts:
            return 0
        total_duration = sum(workout['duration'] for workout in self.workouts)
        return total_duration / self.total_workouts()

    def total_distance(self):
        return sum(workout['distance'] for workout in self.workouts)

    def summary_statistics(self):
        return {
            'total_workouts': self.total_workouts(),
            'average_duration': self.average_duration(),
            'total_distance': self.total_distance(),
        }