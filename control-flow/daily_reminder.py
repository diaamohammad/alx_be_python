#prompt for a single task 

task = input("Enter your task:")

priority = input("Priority (high/medium/low:")

time = input("Is it time-bound? (yes/no):")

match priority:

    case "high":
        
    
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")



    case "medium":
           print(f"Reminder: '{task}' is a {priority} priority task.")



    case "low":
          print(f"Reminder: '{task}' is a {priority} priority task.")

          


        



    