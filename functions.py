import os

# This version switched from repetitive code to introducing custom functions. The older
# version was saved as main-before-using-custom-functions.py (SWS 4/20/2024)

TODO_FILENAME = "todo.txt"

# -------------------------------------------------------------------------------------------------------------------
# Note: To access a directory other than your working one, use an Absolute Path (instead of a Relative Path).
# Example: Windows - file is in C:\Users\sshatz\Downloads\todos.txt
#           file = open(r"C:\Users\sshatz\Downloads\todos.txt", 'r')   # We need a "raw string" (r"") to prevent
#                                                    recognition of coincidental escape chars like '\U' and '\t'
# Example: MacOS/Linux - file is in /Users/stevenshatz/Downloads/todos.txt
#           file = open("/Users/stevenshatz/Downloads/todos.txt")       # No need for r"" with forward slashes
# -------------------------------------------------------------------------------------------------------------------


def get_filepath(filename: str) -> str:
    # Get directory of the currently executing script (e.g., gui.py)
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Use this directory as the base for our file paths
    filepath = os.path.join(script_directory, filename)
    # /Users/stevenshatz/Learn Python in 60 Days/app1/todos.txt

    return filepath


def get_todo_list(from_file=TODO_FILENAME) -> []:
    """
    Read a text file and return the list of todo items.

    :param from_file: the text file holding the list
    :return: the list of todo items (as strings)
    """
    todo_filepath = get_filepath(from_file)
    with open(todo_filepath, 'r') as file_in:
        todos = file_in.readlines()
    return todos


def write_todo_list(todos: [], to_file=TODO_FILENAME):
    """
    Write the list of todo items to a text file.

    :param todos: the list of todo items (as strings)
    :param to_file: the text file holding the list
    :return: None
    """
    todos_filepath = get_filepath(to_file)
    with open(todos_filepath, 'w') as file_out:
        file_out.writelines(todos)
    return


def standardize_action(action: str) -> str:
    """
    Validate an action. If an abbreviation or alias was entered, change it
    to the basic action (i.e., change 'exit' to 'quit'; change 'n do this'
    to 'add do this'; et. al.). In all cases, strip whitespace from the
    front and back of the action and force the action to lowercase.

    Valid Actions:
    - 'add' ('a', 'new', and 'n' are converted to 'add')
    - 'edit' ('e' is converted to 'edit')
    - 'show' ('s', 'display', 'disp', and 'd' are converted to 'show')
    - 'complete' ('c' is converted to 'complete'
    - 'quit' ('q', 'exit', and 'x' are converted to 'quit')

    Some actions may be followed by additional text:
    - 'add read this book' will append the new todo ('Read this book') to the end
        of the list.
    - 'add' will prompt the user to keep entering new todos until user hits return.
    - 'edit 3' will edit the 3rd item in the todo list.
    - 'edit' will prompt the user to keep entering item numbers to be edited until
        user hits return.
    - 'complete 5' will delete the 5th item in the todo list.
    - 'complete' will prompt the user to enter an item number to be deleted. Only 1
        item will be deleted.

    :return: the user-entered action (as a stripped string forced to lower-case)
    """
    # Get user input and strip spaces from it and force to lower-case:

    action = action.lower()

    # Examples of valid actions:
    # --------------------------
    # 1) add -- prompt user for what to add; keep adding items until user enters blank line
    # 2) add play the piano -- no prompt needed; only 1 item added
    # 3) edit -- prompt user for item number to edit; keep editing items until user enters blank line
    # 4) edit 3 -- no prompt needed; only 1 item edited
    # 5) show
    # 6) complete -- prompt user for item number to delete; only 1 item deleted
    # 7) complete 3 -- no prompt needed; only 1 item deleted
    # 8) quit

    if action == 'a':  # Support command abbreviations
        action = 'add'
    elif action.startswith('a '):
        action = 'add ' + action[2:]
    elif action == 's':
        action = 'show'
    elif action == 'e':
        action = 'edit'
    elif action.startswith('e '):
        action = 'edit ' + action[2:]
    elif action == 'c':
        action = 'complete'
    elif action.startswith('c '):
        action = 'complete ' + action[2:]
    elif action == 'q':
        action = 'quit'

    if action == 'new':  # Support command synonyms  (new or n=add; display ,disp, or d=show; exit or x=quit)
        action = 'add'
    elif action.startswith('new '):
        action = 'add ' + action[4:]
    elif action.startswith('n '):
        action = 'add ' + action[2:]
    elif action == 'display' or action == 'disp' or action == 'd':
        action = 'show'
    elif action == 'exit' or action == 'x':
        action = 'quit'

    return action


def capFirst(s: str) -> str:
    """ Capitalize the 1st letter of a string and leave the rest alone """
    return s[:1].upper() + s[1:]


# >>> If uncommented, the following line would get executed when cli.py invokes 'import functions':
# print(f"Hello from functions where __name__ is '{__name__}'")
# >>> If run from cli.py, the above would print: Hello from functions where __name__ is 'functions'
# >>> If run directly from this module, the above would print: Hello from functions where __name__ is '__main__'

# This next statement will be executed only when we run this module, functions.py:
if __name__ == "__main__":
    print("Hello")
    print(get_todo_list())
