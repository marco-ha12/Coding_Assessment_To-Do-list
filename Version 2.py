import tkinter as tk
from tkinter import messagebox, simpledialog
 
# Global list storing all categories
# Each item is a dictionary: {"name": str, "tasks": [{"name": str, "completed": bool}]}
all_categories = []
 
# Tracks which category is currently selected so task buttons always know which one to act on
current_category_index = None
 
 
# Core Functions 
 
def refresh_category_box():
    # Clear and repopulate the category box with current category names.
    category_box.delete(0, tk.END)
    for category in all_categories:
        category_box.insert(tk.END, category["name"])
 
 
def refresh_task_box():
    # Clear and repopulate the task box based on the current category index.
    task_box.delete(0, tk.END)
    if current_category_index is None:
        return
    for task in all_categories[current_category_index]["tasks"]:
        # Show a checkmark if the task is complete
        if task["completed"]:
            task_box.insert(tk.END, f"✔ {task['name']}")
        else:
            task_box.insert(tk.END, task["name"])
 
 
def get_selected_task_index():
    # Return the index of the currently selected task, or None if nothing is selected.
    selection = task_box.curselection()
    if not selection:
        messagebox.showwarning("No task selected", "Please select a task first.")
        return None
    return selection[0]
 
 
# --- Category Management ---
 
def on_category_select(event):
    # Update current_category_index and refresh tasks when user clicks a category.
    global current_category_index
    selection = category_box.curselection()
    if not selection:
        return
    current_category_index = selection[0]
    refresh_task_box()
 
 
def create_category():
    # Ask the user for a category name and create a new empty category.
    category_name = simpledialog.askstring("New Category", "Enter a name for your new category:")
 
    # Reject empty or cancelled input
    if not category_name or category_name.strip() == "":
        messagebox.showwarning("Invalid input", "Category name cannot be empty.")
        return
 
    category_name = category_name.strip()
 
    # Check for duplicate category names
    for category in all_categories:
        if category["name"].lower() == category_name.lower():
            messagebox.showwarning("Duplicate", f"A category called '{category_name}' already exists.")
            return
 
    all_categories.append({"name": category_name, "tasks": []})
    refresh_category_box()
 
 
def delete_category():
    # Delete the currently selected category after confirmation.
    global current_category_index
    if current_category_index is None:
        messagebox.showwarning("No category selected", "Please select a category first.")
        return
 
    category_name = all_categories[current_category_index]["name"]
    confirm = messagebox.askyesno("Delete Category", f"Are you sure you want to delete '{category_name}'?")
    if confirm:
        all_categories.pop(current_category_index)
        current_category_index = None
        task_box.delete(0, tk.END)
        refresh_category_box()
 
 
# Task Management
 
def add_task():
    # Add a new task to the currently selected category.
    if current_category_index is None:
        messagebox.showwarning("No category selected", "Please select a category first.")
        return
 
    task_name = simpledialog.askstring("New Task", "Enter the task:")
 
    # Reject empty or cancelled input
    if not task_name or task_name.strip() == "":
        messagebox.showwarning("Invalid input", "Task cannot be empty.")
        return
 
    # Store task as a dictionary with name and completion status
    all_categories[current_category_index]["tasks"].append({"name": task_name.strip(), "completed": False})
    refresh_task_box()
 
 
def remove_task():
    # Remove the selected task from the currently selected category.
    if current_category_index is None:
        messagebox.showwarning("No category selected", "Please select a category first.")
        return
 
    task_index = get_selected_task_index()
    if task_index is None:
        return
 
    task_name = all_categories[current_category_index]["tasks"][task_index]["name"]
    confirm = messagebox.askyesno("Remove Task", f"Remove task '{task_name}'?")
    if confirm:
        all_categories[current_category_index]["tasks"].pop(task_index)
        refresh_task_box()
 
 
def mark_complete():
    # Mark the selected task as complete by adding a checkmark.
    if current_category_index is None:
        messagebox.showwarning("No category selected", "Please select a category first.")
        return
 
    task_index = get_selected_task_index()
    if task_index is None:
        return
 
    # Set completed to True so the checkmark appears on refresh
    all_categories[current_category_index]["tasks"][task_index]["completed"] = True
    refresh_task_box()
 
 
# GUI Setup 
# Everything below this point builds the actual window and widgets.
# Functions defined above are linked to buttons using command=...
 
# Main window
window = tk.Tk()
window.title("To-Do List App")
window.resizable(False, False)
 
# Left frame: category management
# grid column 0 = left side of the window
left_frame = tk.Frame(window, padx=10, pady=10)
left_frame.grid(row=0, column=0, sticky="ns")
 
tk.Label(left_frame, text="My Categories", font=("Arial", 12, "bold")).pack()
 
# Listbox showing all category names
category_box = tk.Listbox(left_frame, width=25, height=15)
category_box.pack()
category_box.bind("<<ListboxSelect>>", on_category_select)
 
tk.Button(left_frame, text="+ New Category", width=20, command=create_category).pack(pady=2)
tk.Button(left_frame, text="- Delete Category", width=20, command=delete_category).pack(pady=2)
 
# Right frame: task management
# grid column 1 = right side of the window
right_frame = tk.Frame(window, padx=10, pady=10)
right_frame.grid(row=0, column=1, sticky="ns")
 
tk.Label(right_frame, text="Tasks", font=("Arial", 12, "bold")).pack()
 
# Listbox showing tasks for the selected category
task_box = tk.Listbox(right_frame, width=35, height=15)
task_box.pack()
 
tk.Button(right_frame, text="+ Add Task", width=25, command=add_task).pack(pady=2)
tk.Button(right_frame, text="- Remove Task", width=25, command=remove_task).pack(pady=2)
tk.Button(right_frame, text="✔ Mark Complete", width=25, command=mark_complete).pack(pady=2)
 
# Start the GUI event loop
window.mainloop()
