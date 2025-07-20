def add_task(task_list, task):
    task_list.append({"task": task, "done": False})
    return task_list

if __name__ == "__main__":
    tasks = []
    tasks = add_task(tasks, "Learn Git")
    print(tasks)

