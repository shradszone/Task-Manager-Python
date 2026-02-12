def tasks_manager():
    tasks_list = []
    print("task management")

tasks_list = []  
total_task = int(input("enter how many tasks to add:"))
for i in range(1, total_task + 1):
    task_name = input(f"enter task{i}=")
    tasks_list.append(task_name)
print(f"today's task\n{tasks_list}")

while True:
    operation = int(input("enter 1-add\n 2-update\n 3-delete\n 4-view\n 5-exit/stop/"))
    if operation == 1:
        add = input("enter task to add:")
        tasks_list.append(add)
        print(f"task {add} successfully added")
    elif operation == 2:
        updated_val = input("enter task name you want to update:")
        if updated_val in tasks_list:
            up = input("enter new task:") 
            ind = tasks_list.index(updated_val)
            tasks_list[ind] = up
            print(f"updated task {updated_val}")
    elif operation == 3:
        del_val = input("which task you want to delete") 
        if del_val in tasks_list:
            ind = tasks_list.index(del_val)
            del tasks_list[ind]
            print(f"task {del_val} has been deleted")
    elif operation == 4:
        print(f"total tasks = {tasks_list}")
    elif operation == 5:
        print("closing")
        break
    else:
        print("invalid")