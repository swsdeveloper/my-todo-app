import streamlit as st
import functions as fn

# Streamlit is used for web apps. It also integrates well with graphs.
# Installed v1.33.0 via Python Packages icon
#
# Also installed watchdog, since streamlit recommended it for improved performance:
#   xcode-select --install
#   pip install watchdog

todos = fn.get_todo_list()


def add_todo() -> None:
    new_todo = st.session_state["new_todo"]  # Get value of widget with key "new_todo"
    todos.append(new_todo + '\n')
    fn.write_todo_list(todos)
    st.session_state["new_todo"] = ""
    return


def delete_todo(todo_index: int, todo_key: str) -> None:
    try:
        todos.pop(todo_index)           # Throws IndexError if invalid index.
        fn.write_todo_list(todos)
        del st.session_state[todo_key]  # Throws KeyError if key not found.
    except IndexError:
        print(f"IndexError: when attempting to delete item at index: {todo_index}.")
        pass    # Neither todos nor session_state have changed.
    except KeyError:
        print(f"KeyError: when attempting to delete key: {todo_key}.")
        pass    # Todos was updated, but now session_state has a non-existent item.
    return


st.title('My Todo App')

# To run this, open Terminal (in this IDE) and enter:  streamlit run web.py
# This will display the URL of the created web page.
# Look for that URL in your default web browser.
# For me, the URL automatically opened in Firefox when I ran the program.
#
# To see subsequent changes to the website, just refresh the page.
# Each refresh causes the program to run again.

# st.text_input(label="Enter a todo:")          # Text box with label above it
# Streamlit discourages the use of empty labels. Instead provide a label and hide it.

st.text_input("empty", label_visibility='hidden', placeholder="Enter a todo:",
              on_change=add_todo, key="new_todo")  # Text box with 'hint' label inside it

# Sub-header example:
# -------------------
# st.subheader("This is my Todo app.")
# st.subheader("")    # skip a line after Text box

# Text Example:
# -------------
# st.write("This app is meant to increase your productivity.")

# Checkbox Example:
# -----------------
# st.checkbox("Buy groceries.")
# st.checkbox("Throw out the trash.")
#
# Button Example:
# ---------------
# st.button("Add")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        delete_todo(index, todo)
        st.rerun()

# Debugging: To see session_state object, un-rem the next line:
# -------------------------------------------------------------
# st.session_state
