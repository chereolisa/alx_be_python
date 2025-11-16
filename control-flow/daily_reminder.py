task = input("Enter a task description: ").lower()
priority = input("Enter task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound (yes or no): ").lower()

match priority:
    case "high":
            print(f"'{task}' is a high priority task" , end=" ")
    case "medium":
            print(f"'{task}' is a medium priority task" , end=" ")
    case "low":
            print(f"'{task}' is a low priority task" , end=" ")

if time_bound == "yes":
        print("that requires immediate attention today!")
else:
        print("Consider completing it when you have free time.")          