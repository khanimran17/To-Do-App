from functions import read_file, write_file
import time

now = time.strftime("%b %d %Y %I:%M:%S %p")
print("It's is", now)

while True:
    user_input = input('Type add, show, edit, complete or exit: ')
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input[4:]
        todo = todo.title()

        todos = read_file()

        todos.append(todo + '\n')

        write_file(todos)

    elif user_input.startswith('show'):
        todos = read_file()

        # new_todos = []

        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # list comprehension
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos, start=1):
            item = item.strip("\n")
            row = f"{index}.{item}"
            print(row)

    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            number = number - 1

            todos = read_file()

            new_todo = input('Enter new todo: ')
            new_todo = new_todo.title() + '\n'
            todos[number] = new_todo

            write_file(todos)

        except ValueError:
            print('Command is not valid')
            continue

    elif user_input.startswith('complete'):
        try:
            remove = int(user_input[9:])

            todos = read_file()

            index = remove - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            write_file(todos)

            message = f"Todo ({todo_to_remove}) was removed from the list"
            print(message)
        except IndexError:
            print(f'{user_input[9:]} number todo is not added')
            continue
        except ValueError:
            print('Command is not valid, Try writing number')
            continue

    elif user_input.startswith('exit'):
        break

    else:
        print(f"{user_input} Command is Invalid")

print('Bye')
