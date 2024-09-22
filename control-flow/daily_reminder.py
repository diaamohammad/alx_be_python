# Script: daily_reminder.py

# Loop to get valid inputs
while True:
    # Get user inputs for task, priority, and time sensitivity
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Validate inputs for priority and time-bound
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        continue  # Restart loop if invalid priority is entered
    
    if time_bound not in ["yes", "no"]:
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
        continue  # Restart loop if invalid input for time sensitivity
    
    # Process task based on priority using match-case
    match priority:
        case "high":
            priority_message = "a high priority task"
        case "medium":
            priority_message = "a medium priority task"
        case "low":
            priority_message = "a low priority task"
    
    # Add time-bound information using if statement
    if time_bound == "yes":
        time_message = "that requires immediate attention today!"
    else:
        time_message = ""
    
    # Print the customized reminder
    print(f"Reminder: '{task}' is {priority_message} {time_message}")
    
    # Exit the loop after providing a valid reminder
    break


    