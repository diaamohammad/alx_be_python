#prompt for a single task 

Task = input("Enter your task:")

Priority = input("Priority (high/medium/low:")

Time = input("Is it time-bound? (yes/no):")

match priority:

    case "high":
        
    
            print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention today!")



    case "medium":
           print(f"Reminder: '{Task}' is a {Priority} priority task.")



    case "low":
          print(f"Reminder: '{Task}' is a {Priority} priority task.")

          


        



    