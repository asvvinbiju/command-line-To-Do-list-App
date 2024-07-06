import json
import time

class Tasks:
    def __init__(self, description, due_date, completed):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "description": self.description,
            "due_date": self.due_date,
            "status": self.completed
        }
    
    @staticmethod
    def from_dict(task_dict):
        return Tasks(description=task_dict["description"], due_date=task_dict["due_date"], completed=task_dict["status"])


class ToDoList:
    task_dict = []
    try:
        with open("data.json", "r") as fl:
            data = json.load(fl)
            tasks_ = [Tasks.from_dict(task) if task != "" else "" for task in data]
            for task in tasks_:
                task_dict.append(task.to_dict())
    except:
        task_dict = []
    
    def add_task(self, description, due_date):
        self.t = Tasks(description=description, due_date=due_date, completed="incomplete")
        self.task = self.t.to_dict()
        self.task_dict.append(self.task)

    def view_all_tasks(self):
            if self.task_dict == []:
                print("\nYour Task Bar looks lonely!")
                while True:
                    option = input("type 'back' to go back to the menu\n")
                    if option.startswith('b'):
                        break
                    else:
                        print("invalid input!")
                        time.sleep(1)
                        continue
                return 0
            else:
                print("\nThings to do:\n")
                for index, task in enumerate(self.task_dict):
                    desc = task["description"].upper()
                    print( f"[{index + 1}] {desc} on {task["due_date"]} [status - {task["status"]}]", end="\n\n")
                while True:
                    option = input("type 'back' to go back to the menu\n>")
                    if option.startswith('b'):
                        break
                    else:
                        print("invalid input!")
                        time.sleep(1)
                        continue
        
    def mark_task_completed(self):
        is_complete = True
        if self.task_dict == []:
            print("Empty Tasks!")
            time.sleep(1)
            return 0
        print("")
        print("Incomplete tasks:\n")
        for index, tasks in enumerate(self.task_dict):
            if tasks["status"] == "incomplete":
                is_complete = False
                ts = tasks["description"].upper()
                print(f"[{index + 1}] - {ts} on {tasks["due_date"]}\n")
        if is_complete:
            print("No incomplete tasks!")
            time.sleep(1)
            return
        print("Enter task number to mark as completed(type 'back' to return)")
        task_num = input(">")
        if task_num.startswith("b"):
            return 0
        else:
            self.task_dict[int(task_num) - 1].update({"status": "completed"})
            d = self.task_dict[int(task_num) - 1]["description"].upper()
            print(f"{d} Completed, Congratulations!")
            time.sleep(1)
        

    def remove_task(self):
        if self.task_dict == []:
            print("No Tasks to remove!")
            time.sleep(1)
            return 0
        
        print("Tasks:\n")
        for index, task in enumerate(self.task_dict):
            desc = task["description"].upper()
            print( f"[{index + 1}] : {desc} on {task["due_date"]} [status - {task["status"]}]\n")

        print("\nEnter task number to remove(type 'back' to return)")
        self.num = input(">")
        if self.num.startswith('b'):
            return 0
        try:
            self.task_dict.pop(int(self.num) - 1)
        except:
            print("Task do not exist")
            time.sleep(1)
            print("\n")
            main()

    def save_and_exit(self):
        try:
            with open("data.json", "w") as fl:
                json.dump(self.task_dict, fl, indent=4)
        except FileExistsError:
            pass


def main():
    todolist = ToDoList()
    while True:
        print("To Do List:")
        print("[1] Add a task")
        print("[2] View all tasks")
        print("[3] Mark a task as completed")
        print("[4] Remove a task")
        print("[5] Save and exit")
        try:
            option = int(input("Choose an option:"))
        except:
            print("-------------")
            print("**Entered string input!\nplease provide a integer input**")
            print("-------------")
            time.sleep(2)
            continue

        if option==1:
            description = input("enter task description:")
            due_date = input("enter date:")
            todolist.add_task(description, due_date)
        elif option==2:
            todolist.view_all_tasks()
        elif option==3:
            todolist.mark_task_completed()
        elif option==4:
            todolist.remove_task()
        elif option==5:
            todolist.save_and_exit()
            break
        elif option!=[1,2,3,4,5]:
            print("-------------")
            print("***invalid option***")
            print("-------------")
            time.sleep(2)
            continue

if __name__ == "__main__":
    main()