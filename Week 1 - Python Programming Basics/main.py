from datetime import datetime
from common.utils import print_header, print_toc_entry, print_sub_section


# --- Sub-section 4: Exercise 1 (Count Words and Lines) ---
def count_words_and_lines(filename: str) -> None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines: list[str] = file.readlines()
            line_count: int = len(lines)
            word_count: int = sum(len(line.split()) for line in lines)

            print(f"File: '{filename}'")
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# --- Sub-section 5: Exercise 2 (Write and Read List of Items) ---
def write_items_to_file(filename: str, items: list[str]) -> None:
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for item in items:
                file.write(f"{item}\n")
        print(f"Successfully wrote {len(items)} items to '{filename}'.")
    except OSError as e:
        print(f"Error writing to '{filename}': {e}")


def read_items_from_file(filename: str) -> None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            items: list[str] = file.readlines()
            print(f"Items in '{filename}':")
            for item in items:
                print(f"  - {item.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# --- Sub-section 6: Practice 1 (Copy File Contents) ---
def copy_file_contents(source_file: str, destination_file: str) -> None:
    try:
        with open(source_file, "r", encoding="utf-8") as src:
            content: str = src.read()

        with open(destination_file, "w", encoding="utf-8") as dest:
            dest.write(content)

        print(f"Copied contents from '{source_file}' to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: Source file '{source_file}' not found.")


# --- Sub-section 7: Practice 2 (Count Specific Word Occurrences) ---
def count_word_occurrences(filename: str, target_word: str) -> int:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content: str = file.read().lower()
            words: list[str] = [word.strip(".,!?;:\"'()") for word in content.split()]
            return words.count(target_word.lower())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0


# --- Sub-section 8: Practice 3 (Log Messages with Timestamps) ---
def log_message_with_timestamp(log_file: str, message: str) -> None:
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {message}\n")
        print(f"Logged: [{timestamp}] {message}")
    except OSError as e:
        print(f"Error writing to log file '{log_file}': {e}")


def main() -> None:
    print_header("Day 6: File Handling in Python")
    print_toc_entry(1, "Opening, Writing, and Appending Files (open, modes)")
    print_toc_entry(2, "Reading Files (read, readline, readlines)")
    print_toc_entry(3, "Exception Handling (try / except FileNotFoundError)")
    print_toc_entry(4, "Exercise 1: Count Words and Lines in a File")
    print_toc_entry(5, "Exercise 2: Write and Read a List of Items")
    print_toc_entry(6, "Practice 1: Copy Contents from One File to Another")
    print_toc_entry(7, "Practice 2: Count Occurrences of a Specific Word")
    print_toc_entry(8, "Practice 3: Log Messages with Timestamps")

    sample_file: str = "day_6_file_handling/sample.txt"
    fruits_file: str = "fruits.txt"
    copied_file: str = "sample_copy.txt"
    log_file: str = "app_activity.log"

    # 1. Opening, Writing, and Appending Files
    print_sub_section(1, "Opening, Writing, and Appending Files (open, modes)")
    with open(sample_file, "w", encoding="utf-8") as file:
        file.write("Hello World\n")
        file.write("How are you\n")
        file.write("What is the plan for today\n")

    with open(sample_file, "a", encoding="utf-8") as file:
        file.write("Are you working on AI technologies\n")
    print(f"Created and appended lines to '{sample_file}' using 'w' and 'a' modes.")

    # 2. Reading Files (read, readline, readlines)
    print_sub_section(2, "Reading Files (read, readline, readlines)")
    with open(sample_file, "r", encoding="utf-8") as file:
        first_line: str = file.readline().strip()
        print(f"First line (readline): '{first_line}'")

    with open(sample_file, "r", encoding="utf-8") as file:
        all_lines: list[str] = file.readlines()
        print(f"All lines as list (readlines): {[line.strip() for line in all_lines]}")

    # 3. Exception Handling
    print_sub_section(3, "Exception Handling (try / except FileNotFoundError)")
    missing_file: str = "non_existent_file.txt"
    try:
        with open(missing_file, "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Handled gracefully: '{missing_file}' does not exist.")
    except PermissionError:
        print(f"Handled gracefully: Permission denied for '{missing_file}'.")
    except OSError as e:
        print(f"Handled gracefully: I/O error occurred ({e}).")

    # 4. Exercise 1: Count Words and Lines
    print_sub_section(4, "Exercise 1: Count Words and Lines in a File")
    count_words_and_lines(sample_file)

    # 5. Exercise 2: Write and Read a List of Items
    print_sub_section(5, "Exercise 2: Write and Read a List of Items")
    fruits: list[str] = ["Apple", "Banana", "Cherry", "Dates"]
    write_items_to_file(fruits_file, fruits)
    read_items_from_file(fruits_file)
    read_items_from_file("items.txt")  # Triggers FileNotFoundError check from lesson

    # 6. Practice 1: Copy Contents from One File to Another
    print_sub_section(6, "Practice 1: Copy Contents from One File to Another")
    copy_file_contents(sample_file, copied_file)

    # 7. Practice 2: Count Occurrences of a Specific Word
    print_sub_section(7, "Practice 2: Count Occurrences of a Specific Word")
    search_word: str = "are"
    occurrences: int = count_word_occurrences(sample_file, search_word)
    print(f"The word '{search_word}' appears {occurrences} time(s) in '{sample_file}'.")

    # 8. Practice 3: Log Messages with Timestamps
    print_sub_section(8, "Practice 3: Log Messages with Timestamps")
    sample_logs: list[str] = [
        "User started Day 6 file handling script.",
        "Processed sample.txt and fruits.txt successfully."
    ]
    for entry in sample_logs:
        log_message_with_timestamp(log_file, entry)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
