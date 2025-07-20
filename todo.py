def add_task(task_list, task):
    task_list.append({"task": task, "done": False})
    return task_list

if __name__ == "__main__":
    tasks = []
    tasks = add_task(tasks, "Learn Git")
    print(tasks)

def mark_done(task_list, index):
    if 0 <= index < len(task_list):
        task_list[index]["done"] = True
    return task_list

