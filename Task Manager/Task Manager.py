# Import the datetime module
from datetime import datetime


# Define the User class


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Logic to create user object when reading file
    @classmethod
    def from_file(cls, line):
        temp = line.strip()
        temp = temp.replace('"', '')
        parts = temp.split(", ")
        return cls(parts[0], parts[1])

    # Logic to return the user object to the file format
    def to_file(self):
        return f'"{self.username}", "{self.password}"\n'

# Define the Task class


class Task:
    def __init__(
            self, task_holder, task_title, task_description,
            task_assigned, task_due_date, completed):

        self.task_holder = task_holder
        self.task_title = task_title
        self.task_description = task_description
        self.task_assigned = task_assigned
        self.task_due_date = task_due_date
        self.completed = completed

    # Logic to create task object when reading file
    @classmethod
    def from_file(cls, line):
        parts = line.strip().split(", ")
        return cls(parts[0], parts[1], parts[2],
                   parts[3], parts[4], parts[5])

    # Logic to return the task object to the file format
    def to_file(self):
        return (f"{self.task_holder}, {self.task_title}, "
                f"{self.task_description}, {self.task_assigned}, "
                f"{self.task_due_date}, {self.completed}\n")

# Define the helper function to load users as user objects


def load_users():
    user_list = []

    try:
        with open("user.txt", "r") as file:
            for line in file:
                user = User.from_file(line)
                user_list.append(user)
    except FileNotFoundError:
        return []

    return user_list

# Define the helper function to write users to the file


def write_users(user_list):
    with open("user.txt", "w") as file:
        for user in user_list:
            file.write(user.to_file())

# Define the helper function to load tasks as task objects


def load_tasks():
    task_list = []

    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = Task.from_file(line)
                task_list.append(task)
    except FileNotFoundError:
        return []

    return task_list

# Define the helper function to write tasks to the file


def write_tasks(task_list):
    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(task.to_file())


# Define the login function which allows
# users to gain access to the program
def login():
    users = load_users()

    logged_in = False

    while logged_in == False:
        user_name = input("Please enter your username: ")
        user_password = input("Please enter your password: ")

        for user in users:
            if user_name == user.username and user_password == user.password:
                print(f"\nWelcome {user_name}\n")
                logged_in = True
                break

        else:
            print(
                "\nInvalid username or password. Please try again\n")

    return user_name


# Define the function that allows new users to be registered
def reg_user(current_user):
    users = load_users()

    if current_user != "admin":
        print("Only admin can register new users.\n")
        return

    new_username = input("Please enter the new username: ")

    for user in users:
        if user.username == new_username:
            print("The user already exists.")
            return

    confirmed_password = False

    while confirmed_password == False:

        new_password = input(
            "Please enter the password for this user: ")
        confirm_password = input(
            "Please confirm the password by entering it again: ")

        if new_password == confirm_password:

            confirmed_password = True
            break

        else:
            print("Passwords do not match. Please try again.\n")

    new_user = User(new_username, new_password)

    users.append(new_user)

    write_users(users)

    print(f"\nWelcome {new_username}")


# Define the function that allows tasks to be added and assigned
def add_task():
    task_holder = input("Who is responsible for this task?: ")
    task_title = input("What is the title of the task?: ")
    task_description = input("Describe the task: ")

    formatted_date = False
    while not formatted_date:

        user_date = input(
            "What is the due date for this task? (YYYY-MM-DD): ")

        try:
            date_object = datetime.strptime(user_date, "%Y-%m-%d")
            task_due_date = date_object.strftime("%d %b %Y")
            formatted_date = True
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.\n")

    completed = "No"

    task_assigned = datetime.today().strftime("%d %b %Y")

    new_task = Task(task_holder, task_title, task_description, task_assigned,
                    task_due_date, completed)

    tasks = load_tasks()
    tasks.append(new_task)
    write_tasks(tasks)

    print("\nNew task added.\n")

# Define the function that will view all tasks


def view_all():
    tasks = load_tasks()

    for task in tasks:

        print("")
        print(f"Task assigned to    : {task.task_holder}")
        print(f"Task title          : {task.task_title}")
        print(f"Description         : {task.task_description}")
        print(f"Task assigned       : {task.task_assigned}")
        print(f"Due date            : {task.task_due_date}")
        print(f"Completed?          : {task.completed}")
        print("")


# Define the function to view the user's tasks
def view_mine(current_user):
    tasks = load_tasks()
    my_tasks = []

    for task in tasks:
        if task.task_holder == current_user:
            my_tasks.append(task)

    if not my_tasks:
        print("\nYou have no tasks.\n")
        return

    task_number = 1

    for task in my_tasks:
        print(f"\nTask {task_number}")
        print(f"Task assigned to    : {task.task_holder}")
        print(f"Task title          : {task.task_title}")
        print(f"Description         : {task.task_description}")
        print(f"Task assigned       : {task.task_assigned}")
        print(f"Due date            : {task.task_due_date}")
        print(f"Completed?          : {task.completed}")
        print("")

        task_number += 1

    while True:
        try:
            selection = int(
                input("Please enter a number to select that task"
                      "(-1 to return to main menu): "))

            if selection == -1:
                return

            elif 1 <= selection <= len(my_tasks):
                selected_task = my_tasks[selection - 1]

                print("\nYou selected this task:\n")
                print(f"Task assigned to    : {selected_task.task_holder}")
                print(f"Task title          : {selected_task.task_title}")
                print(
                    f"Description         : {selected_task.task_description}")
                print(f"Task assigned       : {selected_task.task_assigned}")
                print(f"Due date            : {selected_task.task_due_date}")
                print(f"Completed?          : {selected_task.completed}")
                print("")

                if selected_task.completed == "Yes":
                    print("Task completed and cannot be edited.\n")
                    return

                print("1 - Mark as complete")
                print("2 - Edit task")
                print("-1 - Return to menu")

                task_edit = input("Select an option: ")

                if task_edit == "1":

                    for task in tasks:
                        if (task.task_holder == selected_task.task_holder and
                            task.task_title == selected_task.task_title and
                                task.task_assigned == selected_task.task_assigned):

                            task.completed = "Yes"
                            break

                    write_tasks(tasks)

                    print("\nThe task has been completed\n")
                    return

                if task_edit == "2":

                    print("\nPlease select the change you would like to make:\n")
                    print("1 - Change assigned user")
                    print("2 - Change due date")

                    edit_choice = input("Select an option: ")

                    for task in tasks:
                        if (task.task_holder == selected_task.task_holder and
                            task.task_title == selected_task.task_title and
                                task.task_assigned == selected_task.task_assigned):

                            if edit_choice == "1":
                                new_user = input(
                                    "Enter the name of the new user responsible for this task: ")
                                task.task_holder = new_user

                            elif edit_choice == "2":

                                while True:
                                    new_date = input(
                                        "Enter new due date (YYYY-MM-DD): ")

                                    try:
                                        date_object = datetime.strptime(
                                            new_date, "%Y-%m-%d")
                                        task.task_due_date = date_object.strftime(
                                            "%d %b %Y")
                                        break
                                    except ValueError:
                                        print("Invalid format. Use YYYY-MM-DD.")

                            break

                    write_tasks(tasks)

                    print("\nTask successfully updated.\n")
                    return

                elif task_edit == "-1":
                    return
            else:
                print("Invalid task number. Try again.\n")

        except ValueError:
            print("Please enter a valid number.\n")


# Define function to view completed tasks
def view_completed():
    print("\nThe following tasks have been completed: \n")

    tasks = load_tasks()

    for task in tasks:
        if task.completed == "Yes":
            print(f"Task assigned to    : {task.task_holder}")
            print(f"Task title          : {task.task_title}")
            print(f"Description         : {task.task_description}")
            print(f"Task assigned       : {task.task_assigned}")
            print(f"Due date            : {task.task_due_date}\n")

# Define function to delete tasks


def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("\nThere are no tasks to delete.\n")
        return

    print("\nSelect a task to delete:\n")

    for index, task in enumerate(tasks, start=1):
        print(f"\nTask {index}")
        print(f"Title: {task.task_title}")
        print(f"Assigned to: {task.task_holder}")

    try:
        selection = int(
            input('Enter the task number to delete. Enter "-1" to cancel: '))
    except ValueError:
        print("\nInput is invalid.\n")
        return

    if selection == -1:
        print("\nNo task deleted.\n")
        return

    if selection < 1 or selection > len(tasks):
        print("\nTask number is invalid.\n")
        return

    tasks.pop(selection - 1)

    write_tasks(tasks)

    print("\nTask deleted.\n")


# Define function to generate reports
def generate_reports():
    completed_tasks = []
    uncompleted_tasks = []
    overdue = []

    today = datetime.today()

    tasks = load_tasks()

    for task in tasks:

        due_date_object = datetime.strptime(task.task_due_date, "%d %b %Y")

        if task.completed == "Yes":
            completed_tasks.append(task)

        else:
            uncompleted_tasks.append(task)

            if due_date_object < today:
                overdue.append(task)

    total_tasks = len(completed_tasks) + len(uncompleted_tasks)
    total_completed = len(completed_tasks)
    total_uncompleted = len(uncompleted_tasks)
    total_overdue = len(overdue)

    if total_tasks > 0:
        percent_completed = (total_completed / total_tasks) * 100
        percent_uncompleted = (total_uncompleted / total_tasks) * 100
        percent_overdue = (total_overdue / total_tasks) * 100
    else:
        percent_completed = 0
        percent_uncompleted = 0
        percent_overdue = 0

    with open("task_overview.txt", "w") as file:

        file.write("Task Report:\n")
        file.write("." * 40 + "\n")
        file.write(f"{'Total tasks:':<30}{total_tasks:>5}\n")
        file.write(f"{'Completed tasks:':<30}{total_completed:>5}\n")
        file.write(f"{'Uncompleted tasks:':<30}{total_uncompleted:>5}\n")
        file.write(f"{'Overdue tasks:':<30}{total_overdue:>5}\n")
        file.write(
            f"{'Percentage completed:':<30}{percent_completed:>5.2f}%\n")
        file.write(
            f"{'Percentage uncompleted:':<30}{percent_uncompleted:>5.2f}%\n")
        file.write(f"{'Percentage overdue:':<30}{percent_overdue:>5.2f}%\n")

    print("\nReport generated.\n")

# Define function to see user overview


def display_statistics():
    generate_reports()

    users_registered = load_users()

    tasks_generated = load_tasks()

    total_users = len(users_registered)

    total_tasks = len(tasks_generated)

    today = datetime.today()

    with open("user_overview.txt", "w") as file:
        file.write("User Overview\n")
        file.write("." * 40 + "\n")
        file.write(f"Total users: {total_users}\n")
        file.write(f"Total tasks: {total_tasks}\n")
        file.write("\n")

        for user in users_registered:
            user_tasks = [
                task for task in tasks_generated if task.task_holder == user.username]
            user_total = len(user_tasks)

            if total_tasks > 0:
                total_percent = (user_total / total_tasks) * 100
            else:
                total_percent = 0

            completed = 0
            incomplete = 0
            overdue = 0

            for task in user_tasks:
                due_date_object = datetime.strptime(
                    task.task_due_date, "%d %b %Y")

                if task.completed == "Yes":
                    completed += 1
                else:
                    incomplete += 1

                    if due_date_object < today:
                        overdue += 1

            if user_total > 0:
                percent_completed = (completed / user_total) * 100
                percent_incomplete = (incomplete / user_total) * 100
                percent_overdue = (overdue / user_total) * 100

            else:
                percent_completed = 0
                percent_incomplete = 0
                percent_overdue = 0

            file.write(f"{'User:':<30}{user.username:>5}\n")
            file.write(f"{'Total tasks assigned:':<30}{user_total:>5}\n")
            file.write(
                f"{'Percentage of total tasks:':<30}{total_percent:5.2f}%\n")
            file.write(
                f"{'Percentage completed:':<30}{percent_completed:5.2f}%\n")
            file.write(
                f"{'percentage incomplete:':<30}{percent_incomplete:5.2f}%\n")
            file.write(f"{'Percent overdue:':<30}{percent_overdue:5.2f}%\n")
            file.write("\n")

    print_reports()


# Define function to print task overview
def print_reports():

    print("\nREPORTS\n")

    try:
        with open("task_overview.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("Task overview file not found.\n")

    print("")

    try:
        with open("user_overview.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("User overview file not found.\n")


# Call login
current_user = login()


# This is the menu the user interacts with
while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    if current_user == "admin":

        print("\nPlease select one of the following options:")
        print("r - to register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("vc - view completed tasks")
        print("del - delete tasks")
        print("ds - display statistics")
        print("gr - generate reports")
        print("e - exit\n")

    else:
        print("\nPlease select one of the following options:")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("e - exit\n")

    menu = input("Type your selection here: ").lower()

    if menu == "r" and current_user == "admin":
        reg_user(current_user)

    elif menu == "vc" and current_user == "admin":
        view_completed()

    elif menu == "del" and current_user == "admin":
        delete_task()

    elif menu == "ds" and current_user == "admin":
        display_statistics()

    elif menu == "gr" and current_user == "admin":
        generate_reports()

    elif menu == "a":
        add_task()

    elif menu == "va":
        view_all()

    elif menu == "vm":
        view_mine(current_user)

    elif menu == "e":
        print("Program closed")
        exit()

    else:
        print("You have entered an invalid input. Please try again")
