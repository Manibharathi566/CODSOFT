def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)
    


todos = []

while True:
    user_action = input("Enter your option ADD,SHOW,REPLACE,COMPLETE and EXIT").strip().lower()

    if 'add' in user_action:
        todo = user_action[4:] + "\n"
        todos.append(todo)
        write_todos(todos)

    elif 'show' in user_action:
        todos = get_todos()
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos, 100):
            print(index, item)

    elif 'complete' in user_action:
        try:
            removeindex = int(user_action[9:])
            todos.pop(removeindex - 1)
            write_todos(todos)
        except IndexError:
            print("no item in todo list")
            


    elif 'replace' in user_action:
        try:
            listindex = int(user_action[8:]) 
            todos = get_todos()
            new_item = input("Enter your replace todo item") + "\n"
            todos[listindex] = new_item + "\n" 
            write_todos(todos)
        except ValueError:
            print("your input is wrong")
            continue
    
    elif 'exit' in user_action:
        break

    else:
        print("command is not valid")

print("quit")