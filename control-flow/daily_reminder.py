Task = input("Enter your task:")
Priority = input("Priority (high/medium/low): ").lower()
Time_bound = input("Is it time-bound? (yes/no): ").lower()

match Priority:
    case "high":
        if Time_bound=="yes".lower():
            print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")

        else:
            print(f"Reminder: '{Task}' is a high priority task, but not time-sensitive.")


    case "medium":
        if Time_bound=="yes".lower():
            print(f"Reminder: '{Task}' is a medium priority task. Complete it soon as it's time-sensitive.")

        else:
            print(f"Reminder: '{Task}' is a medium priority task. Do it at your earliest convenience.")
    
    
    
    case "low":
        if Time_bound=="yes".lower():
            print(f"Reminder: '{Task}' is a low priority task, but it's time-sensitive. Try to complete it today.")
        
        else:
            print(f"Note: '{Task}' is a low priority task. Consider completing it when you have free time.")

    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
        