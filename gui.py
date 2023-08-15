import functions
import PySimpleGUI
import time
import os

if not os.path.exists("todos.txt"):
    with open('todos.txt', 'w') as file:
        pass

PySimpleGUI.theme("black")
clock = PySimpleGUI.Text("",key='clock')
label = PySimpleGUI.Text("Type in a to-do:")
user_input = PySimpleGUI.InputText(tooltip="Enter todo", key='todo',)
add_button = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=functions.read_file(), key='items',
                               enable_events=True, size=[44, 9])
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window('My To-Do App',
                            layout=[[clock],
                                    [label],
                                    [user_input, add_button],
                                    [list_box, edit_button, complete_button],
                                    [exit_button]],
                            font=("Helvetica", 13))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d %Y %I:%M:%S %p"))
    match event:
        case 'Add':
            todos = functions.read_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_file(todos)
            window['items'].update(values=todos)
            window['todo'].update(value="")

        case 'Edit':
            try:
                todo_to_edit = values['items'][0]
                new_todo = values['todo']

                todos = functions.read_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_file(todos)
                window['items'].update(values=todos)
            except IndexError:
                PySimpleGUI.popup("Please Select an Item First.", font=("Helvetica", 13))

        case 'Complete':
            try:
                todo_to_complete = values['items'][0]
                todos = functions.read_file()
                todos.remove(todo_to_complete)
                functions.write_file(todos)
                window['items'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                PySimpleGUI.popup("Please Select an Item First.", font=("Helvetica", 13))

        case 'Exit':
            break

        case 'items':
            window['todo'].update(value=values['items'][0])

        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
