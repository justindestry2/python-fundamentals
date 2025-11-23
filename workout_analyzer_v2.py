def get_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            print("Please enter a positive whole number.")
        except ValueError:
            print("Please enter a whole number (for example: 10).")


def get_positive_float(prompt):

    while True:
        try:
            num = float(input(prompt))
            if num > 0:
                return num
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a number (for example: 7.5).")


def get_exercise_name():

    while True:
        name = input("Enter exercise name (or 'done' to finish): ").strip()

        if name.lower() == "done":
            return "done"

        if name != "":
            return name

        print("Name cannot be empty.")


def exercise_questions():

    workouts = []

    while True:
        name = get_exercise_name()
        if name == "done":
            break

        minutes = get_positive_int("How many minutes? ")
        cal_per_min = get_positive_float("How many calories per minute? ")

        workout_summary = {
            "exercise": name,
            "minutes": minutes,
            "cal_per_min": cal_per_min,
        }

        workouts.append(workout_summary)

    return workouts


def summarize_workouts(workouts):
 
    if not workouts:
        print("No exercises entered.")
        return

    total_minutes = 0
    total_calories = 0
    longest_exercise = workouts[0]

    for w in workouts:
        total_minutes += w["minutes"]
        total_calories += w["minutes"] * w["cal_per_min"]

        if w["minutes"] > longest_exercise["minutes"]:
            longest_exercise = w

    print(f"\n--- Workout Summary ---")
    print(f"Total minutes: {total_minutes}")
    print(f"Total calories: {total_calories}")
    print(f"Longest exercise: {longest_exercise['exercise']} ({longest_exercise['minutes']} min)")


def main():
    workouts = exercise_questions()
    summarize_workouts(workouts)


if __name__ == "__main__":
    main()