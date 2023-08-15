import streamlit as st
import functions

todos = functions.read_file()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_file(todos)


st.title("To-Do App")
st.write("Your todo list:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter new To-do",
              on_change=add_todo, key="new_todo")
print("hello")
