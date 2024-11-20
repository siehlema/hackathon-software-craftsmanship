from typing import List

def get_external_tasks():
    # don't implement this!
    # this function mocks the response of an external data source
    return []

class Task:
    task_name: str
    done: bool

class AnnoyedToDoList:
    def __init__(self):
        self.tasks: List[Task] = []
        self.unfinished_tasks = 0

    def add_task(self, task_name):
        """
        Function that adds a task to the task list
        """
        if type(task_name) != str:
           print("wwrong output")
           return
        if len(self.tasks) > 2:
            print("Woah! That's a lot of tasks! Ever heard of work-life balance? Not doing this ..")
            return
        else:
            print("Yeah, alright. This time I'll add it to the list ...")
        if any([task.task_name == task_name for task in self.tasks]):
           print("You've already added this task!")
           return    
        new_task = Task()
        new_task.task_name = task_name
        new_task.done = False
        self.tasks.append(new_task)
        print(f"Task '{task_name}' added.")
        self.unfinished_tasks += 1

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.task_name == task_name and not task.done:
                task.done = True
                self.unfinished_tasks -= 1
                print(f"Task '{task_name}' completed.")
                if self.unfinished_tasks == 0:
                    print("Wow! You finished all your tasks. Are you sure you're not a robot?")
                return
        print(f"Task '{task_name}' not found or already completed.")

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("Nothing to do! Go binge-watch a show or something.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Done" if task.done == True else "Not Done"
                print(f"{i+1}. {task.task_name} - {status}")

    def delete_task(self, task_name):
        # the annoyed todo list does not want to delete your task
        # time for you to impl this functionality + test in Übung 2
        if not any([task.task_name == task_name for task in self.tasks]):
           print("Task does not exist!")
           return
        self.tasks = [x for x in self.tasks if not x.task_name == task_name]
        print(f"I  deleted the task '{task_name}' :)")


    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks cleared! Now you're free... or are you?")

    def import_tasks_from_external(self):
        external_tasks = get_external_tasks()
        for task in external_tasks:
            self.add_task(task)
        print(f"Imported {len(external_tasks)} tasks from external source.")
