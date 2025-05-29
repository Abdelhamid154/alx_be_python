def daily_reminder():
    print("Welcome to your Daily Task Reminder!")
    print("Please enter your priority task for today.\n")
    
    # Get user input
    task = input("Enter your task: ")
    
    # Validate priority input
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ['high', 'medium', 'low']:
            break
        print("Invalid input. Please enter 'high', 'medium', or 'low'.")
    
    # Validate time-bound input
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ['yes', 'no']:
            break
        print("Invalid input. Please enter 'yes' or 'no'.")
    
    print("\n--- Your Reminder ---")
    
    # Process task based on priority using match case
    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"URGENT: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Important: '{task}' is a high priority task. Focus on this soon.")
        case 'medium':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a medium priority task with a deadline. Try to complete it today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Schedule time for it this week.")
        case 'low':
            if time_bound == 'yes':
                print(f"Gentle reminder: '{task}' is a low priority task but has a time constraint.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

# Run the reminder
daily_reminder()