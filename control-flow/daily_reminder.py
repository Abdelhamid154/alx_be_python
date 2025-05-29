# daily_reminder.py

task = input("Enter your task: ")
priority = input("Enter the priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Task '{task}' is high priority"
    case "medium":
        reminder = f"Task '{task}' is medium priority"
    case "low":
        reminder = f"Task '{task}' is low priority"
    case _:
        reminder = f"Task '{task}' has an unknown priority"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"

print(reminder)
