task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
            print(f"Reminder: '{task}' is a {priority} priority task" , end=" ")
    case "medium":
            print(f"Reminder: '{task}' is a {priority} priority task" , end=" ")
    case "low":
            print(f"Reminder: '{task}' is a {priority} priority task" , end=" ")

if time_bound == "yes":
        print("that requires immediate attention today!")
else:
        print("Consider completing it when you have free time.")          