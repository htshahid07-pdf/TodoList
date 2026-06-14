#store tasks in list
my_tasks = []

#add tasks to list
def add_tasks():
 while True:
    task = input("Enter your tasks for the day, (or enter done to stop)")
    if task == "done":
        break
    else:
     my_tasks.append(task)

#view tasks
def view_tasks():
    for i , task in enumerate(my_tasks, start=1):
     print(i, task)

def main():
   add_tasks()
   view_tasks()

if __name__ == "__main__":
    main()