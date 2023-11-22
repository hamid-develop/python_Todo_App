print("\n Command Line To Do Application")
print("\n ==============================")

select_list = ["-l List all the tasks", "-a Add a new task",
               "-r Remove a task", "-c Complete a task"]

tasks_file = open("tasks.txt", "r")

for value in select_list:
    print(value)

tasks = []


def add(text):
    tasks.append(dict(
        text=text or input(" "),
        state="pending",
    ))
    with open("tasks.txt", 'a') as file:
        file.write(f"{text}\n")


def task_list():
    with open("tasks.txt", 'r') as file:
        all_tasks = file.readlines()
        print(all_tasks)
    # for task in tasks:
    #     print(task['text'])


def remove():
    pass


def completed():
    pass


def menue():
    while True:
        cmd, arg = input("").split(" ", 2)
        
        match(cmd):
            case "-l":
                task_list()
            case "-a":
                add(arg)
            case "-r":
                print("remove")
            case "-c":
                print("completed")
            case _:
                print("Invalid select")


menue()
