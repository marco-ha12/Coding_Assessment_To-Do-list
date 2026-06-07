# Empty list
all_lists =[]

# Displays main menu
def display_menu():
    """Print the main menu options."""
    print("\n===== TO-DO LIST =====")
    print("1. Create a new list")
    print("2. View all lists")
    print("3. Add a task")
    print("4. Exit")
    print("======================")
    
# Creating a list
def create_list():
    
       
    # Ask the user for a list name - remove any unecessary spaces
    list_name = input("Enter a name for your new list : ").strip()

    # Reject empty or whitespace-only input
    if list_name == "":
        print("The name of the list cannot be empty")
        return
    
    # Add a new dictionary to all_lists with an empty task list
    all_lists.append({"name": list_name, "tasks": []})
    print(f"List '{list_name}' created.")


# Display all lists and their tasks
def view_lists():

    # Check if there are any lists before trying to display them
    if len(all_lists) == 0:
        print("No lists found, Create a list first.")
        return
     
    # Loop through each list and print its name and tasks
    for i in range(len(all_lists)):
        print(f"\n{i + 1}. {all_lists[i]['name']}")
        
        # If the task list is empty, show a placeholder message
        if len(all_lists[i]["tasks"]) == 0:
            print("(no tasks yet)")
        else:
            # Print each task with a dash in front
            for j in range(len(all_lists[i]["tasks"])):
                print(f"-{all_lists[i]["tasks"][j]}")

# Add a task to a list chosen by the user.
def add_task():

    # Cannot add a task if no lists exist yet
    if len(all_lists) == 0:
        print("No lists available. Create a list first!")
        return
    
    # Show the lists so the user knows what number to pick
    view_lists()
    
    try:
        choice = int(input("\nEnter the list number to add a task to: "))
        
        # Check the number is within the valid range of list indexes
        if choice < 1 or choice > len(all_lists):
            print("Invalid choice")
            return
        
        task = input("Enter the task: ").strip()

        # Reject empty or whitespace-only task names
        if task == "":
            print("Task cannot be empty.")
            return

        # Append the task string to the chosen list's task list
        all_lists[choice - 1]["tasks"].append(task)
        print(f"Task '{task}' added.")
        
    except ValueError:
        
        # Runs if the user types something that isn't a number
        print("Please enter a valid number")


# Main program loop
print("Welcome to the To-Do List App!")

running = True # Boolean - True/False
while running:
    display_menu()
    user_choice = input("Enter your choice: ").strip()

    # Route the user to the correct function based on their menu choice
    if user_choice == "1":
        create_list()
    elif user_choice == "2":
        view_lists()
    elif user_choice == "3":
        add_task()
    elif user_choice == "4":
        print("Goodbye!")
        running = False # Exit the loop and end the program 
    else:
        # Catches anything that isn't 1, 2, 3, or 4
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        


