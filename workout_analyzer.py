def exercise_questions():
    """Ask the user about their exercises and return a list of workout dicts."""
    exercise_count = int(input("How many exercises did you do? "))
    workouts = []

    for _ in range(exercise_count):
        name = input("What is the exercise name? ")
        minutes = int(input("How many minutes? "))
        cal_per_min = float(input("How many calories for this exercise per minute? "))

        workout_summary = {
            "exercise": name,
            "minutes": minutes,
            "cal_per_min": cal_per_min,
        }

        workouts.append(workout_summary)

    return workouts


def summarize_workouts(workouts):
    """Print a summary: total minutes, total calories, and longest exercise."""
    total_minutes = 0
    total_calories = 0
    longest_exercise = None

    for w in workouts:
        total_minutes += w["minutes"]
        total_calories += w["minutes"] * w["cal_per_min"]

        if longest_exercise is None or w["minutes"] > longest_exercise["minutes"]:
            longest_exercise = w

    print(f"Total minutes: {total_minutes}")
    print(f"Total calories: {total_calories}")
    print(f"Longest exercise: {longest_exercise['exercise']}")


def main():
    workouts = exercise_questions()
    summarize_workouts(workouts)


if __name__ == "__main__":
    main()