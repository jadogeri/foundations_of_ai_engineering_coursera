import csv
import json
import os
import sys
from functools import reduce
from typing import Any, Callable
from common.utils import print_header, print_toc_entry, print_sub_section

TASKS_FILE: str = "tasks.txt"


# --- Sub-section 5: Hands-on Project (Command-Line Task Manager) ---
def load_tasks(filename: str = TASKS_FILE) -> dict[int, dict[str, str]]:
    tasks: dict[int, dict[str, str]] = {}
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts: list[str] = line.strip().split(" | ")
                if len(parts) >= 3:
                    task_id: int = int(parts[0])
                    tasks[task_id] = {
                        "title": parts[1],
                        "status": parts[2],
                        "priority": parts[3] if len(parts) > 3 else "Medium",
                        "deadline": parts[4] if len(parts) > 4 else "None"
                    }
    return tasks


def save_tasks(tasks: dict[int, dict[str, str]], filename: str = TASKS_FILE) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        for task_id, task in tasks.items():
            file.write(
                f"{task_id} | {task['title']} | {task['status']} | "
                f"{task['priority']} | {task['deadline']}\n"
            )


def add_task(
    tasks: dict[int, dict[str, str]],
    title: str,
    priority: str = "Medium",
    deadline: str = "None"
) -> None:
    task_id: int = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {
        "title": title,
        "status": "incomplete",
        "priority": priority,
        "deadline": deadline
    }
    print(f"Task '{title}' (ID: {task_id}) added.")


def view_tasks(tasks: dict[int, dict[str, str]]) -> None:
    if not tasks:
        print("No tasks available.")
        return

    for task_id, task in tasks.items():
        print(
            f"[{task_id}] {task['title']} - Status: {task['status']} "
            f"| Priority: {task['priority']} | Deadline: {task['deadline']}"
        )


def mark_task_complete(tasks: dict[int, dict[str, str]], task_id: int) -> None:
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print(f"Task ID {task_id} not found.")


def delete_task(tasks: dict[int, dict[str, str]], task_id: int) -> None:
    if task_id in tasks:
        deleted_task: dict[str, str] = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print(f"Task ID {task_id} not found.")


# --- Sub-section 6: Practice Bonus (Export to JSON and CSV) ---
def export_tasks_to_json(tasks: dict[int, dict[str, str]], json_file: str = "tasks.json") -> None:
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
    print(f"Exported {len(tasks)} tasks to '{json_file}'.")


def export_tasks_to_csv(tasks: dict[int, dict[str, str]], csv_file: str = "tasks.csv") -> None:
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Status", "Priority", "Deadline"])
        for task_id, task in tasks.items():
            writer.writerow([
                task_id,
                task["title"],
                task["status"],
                task["priority"],
                task["deadline"]
            ])
    print(f"Exported {len(tasks)} tasks to '{csv_file}'.")


def run_interactive_cli() -> None:
    tasks: dict[int, dict[str, str]] = load_tasks()
    while True:
        print("\nTask Manager Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Export Tasks (JSON & CSV)")
        print("6. Save & Exit")

        choice: str = input("Enter your choice: ").strip()

        if choice == "1":
            title: str = input("Enter task title: ").strip()
            priority: str = input("Enter priority (Low/Medium/High): ").strip() or "Medium"
            deadline: str = input("Enter deadline (YYYY-MM-DD or None): ").strip() or "None"
            add_task(tasks, title, priority, deadline)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            try:
                task_id: int = int(input("Enter task ID to mark as complete: "))
                mark_task_complete(tasks, task_id)
            except ValueError:
                print("Please enter a valid numeric ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(tasks, task_id)
            except ValueError:
                print("Please enter a valid numeric ID.")
        elif choice == "5":
            export_tasks_to_json(tasks)
            export_tasks_to_csv(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def main() -> None:
    print_header("Day 7: Pythonic Code and Project Work")
    print_toc_entry(1, "List Comprehensions")
    print_toc_entry(2, "Lambda Functions (Anonymous Functions)")
    print_toc_entry(3, "Functional Built-ins (map, filter, reduce)")
    print_toc_entry(4, "System & OS Modules (os & sys)")
    print_toc_entry(5, "Project: Command-Line Task Manager Demo")
    print_toc_entry(6, "Bonus Features: JSON & CSV Export")

    # 1. List Comprehensions
    print_sub_section(1, "List Comprehensions")
    squares: list[int] = [x ** 2 for x in range(10)]
    evens: list[int] = [x for x in range(10) if x % 2 == 0]
    odds: list[int] = [x for x in range(10) if x % 2 != 0]
    print(f"Squares (0-9): {squares}")
    print(f"Even numbers (0-9): {evens}")
    print(f"Odd numbers (0-9): {odds}")

    # 2. Lambda Functions
    print_sub_section(2, "Lambda Functions (Anonymous Functions)")
    add: Callable[[int, int], int] = lambda x, y: x + y
    print(f"Lambda add(3, 5): {add(3, 5)}")

    # 3. Functional Built-ins (map, filter, reduce)
    print_sub_section(3, "Functional Built-ins (map, filter, reduce)")
    numbers: list[int] = [1, 2, 3, 4]
    mapped_squares: list[int] = list(map(lambda x: x ** 2, numbers))
    filtered_evens: list[int] = list(filter(lambda x: x % 2 == 0, numbers))
    product: int = reduce(lambda x, y: x * y, numbers)

    print(f"Original numbers: {numbers}")
    print(f"map (squares): {mapped_squares}")
    print(f"filter (evens): {filtered_evens}")
    print(f"reduce (product): {product}")

    # 4. System & OS Modules
    print_sub_section(4, "System & OS Modules (os & sys)")
    print(f"Current working directory (os.getcwd): {os.getcwd()}")
    print(f"Script arguments (sys.argv): {sys.argv}")
    print(f"Python version (sys.version): {sys.version.split()[0]}")

    test_dir: str = "test_directory"
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)
        print(f"Created directory: '{test_dir}'")
    os.rmdir(test_dir)
    print(f"Cleaned up directory: '{test_dir}'")

    # 5. Project: Command-Line Task Manager Demo
    print_sub_section(5, "Project: Command-Line Task Manager Demo")
    tasks: dict[int, dict[str, str]] = {}
    add_task(tasks, "Buy milk", priority="High", deadline="2026-11-24")
    add_task(tasks, "Buy eggs", priority="Medium", deadline="2026-11-24")
    add_task(tasks, "Get car wash", priority="Low", deadline="2026-11-25")

    print("\nViewing all tasks:")
    view_tasks(tasks)

    print("\nUpdating and deleting tasks:")
    mark_task_complete(tasks, 2)
    delete_task(tasks, 1)

    print("\nFinal task list:")
    view_tasks(tasks)
    save_tasks(tasks)

    # 6. Bonus Features: JSON & CSV Export
    print_sub_section(6, "Bonus Features: JSON & CSV Export")
    export_tasks_to_json(tasks)
    export_tasks_to_csv(tasks)

    # Uncomment below to launch the interactive CLI menu:
    # run_interactive_cli()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
