from common.utils import print_header, print_toc_entry, print_sub_section


def count_word_frequency(sentence: str) -> dict[str, int]:
    words: list[str] = sentence.split()
    word_count: dict[str, int] = {}

    for word in words:
        cleaned_word: str = word.lower()
        if cleaned_word in word_count:
            word_count[cleaned_word] += 1
        else:
            word_count[cleaned_word] = 1

    return word_count


def reverse_and_deduplicate(items: list[int]) -> list[int]:
    reversed_items: list[int] = items[::-1]
    unique_items: list[int] = list(set(reversed_items))
    return unique_items


def calculate_average_grade(grades: dict[str, float]) -> float:
    if not grades:
        return 0.0
    return sum(grades.values()) / len(grades)


def main() -> None:
    print_header("Day 4: Data Structures (Lists, Tuples, Dictionaries, Sets)")
    print_toc_entry(1, "Lists (Creation, Indexing, Modifying, Slicing)")
    print_toc_entry(2, "Tuples (Immutability & Indexing)")
    print_toc_entry(3, "Dictionaries (Key-Value Pairs & Iteration)")
    print_toc_entry(4, "Sets (Unique Items & Set Operations)")
    print_toc_entry(5, "Exercise 1: Manipulating Data in a Dictionary")
    print_toc_entry(6, "Exercise 2: Word Frequency Counter")
    print_toc_entry(7, "Practice 1: Reverse List & Remove Duplicates")
    print_toc_entry(8, "Practice 2: Student Average Grade Calculator")

    # 1. Lists
    print_sub_section(1, "Lists (Creation, Indexing, Modifying, Slicing)")
    numbers: list[int] = [1, 2, 3, 4]
    fruits: list[str] = ["apple", "banana", "cherry"]
    mixed: list[int | str | bool] = [1, "apple", True]

    print(f"Numbers list: {numbers} | Third element (index 2): {numbers[2]}")
    print(f"Fruits list: {fruits} | First element: {fruits[0]} | Last element (-1): {fruits[-1]}")
    print(f"Mixed list: {mixed} | Second element: {mixed[1]}")

    # Modifying lists
    fruits.append("orange")
    fruits.insert(1, "grape")
    print(f"After append & insert: {fruits}")

    fruits.remove("banana")
    del fruits[0]
    popped_fruit: str = fruits.pop()
    print(f"After remove('banana'), del[0], and pop('{popped_fruit}'): {fruits}")

    # Slicing lists
    sample_fruits: list[str] = ["apple", "grape", "banana", "cherry", "orange"]
    sliced_fruits: list[str] = sample_fruits[1:4]
    print(f"Sliced fruits [1:4]: {sliced_fruits}")

    # 2. Tuples
    print_sub_section(2, "Tuples (Immutability & Indexing)")
    colors: tuple[str, str, str] = ("red", "green", "blue")
    single_item_tuple: tuple[str] = ("glass",)

    print(f"Colors tuple: {colors}")
    print(f"First color (index 0): {colors[0]} | Last color (-1): {colors[-1]}")
    print(f"Single item tuple: {single_item_tuple} (type: {type(single_item_tuple).__name__})")

    # 3. Dictionaries
    print_sub_section(3, "Dictionaries (Key-Value Pairs & Iteration)")
    student: dict[str, str | int] = {
        "name": "Alice",
        "age": 25,
        "grade": "A"
    }
    print(f"Original student: {student}")
    print(f"Student name: {student['name']}")

    # Adding, updating, and removing keys
    student["subject"] = "Math"
    student["age"] = 32
    print(f"After adding subject & updating age: {student}")

    del student["grade"]
    removed_subject: str | int = student.pop("subject")
    print(f"After del['grade'] & pop('{removed_subject}'): {student}")

    # Iterating over a dictionary
    print("Iterating through student items:")
    for key, value in student.items():
        print(f"  {key}: {value}")

    # 4. Sets
    print_sub_section(4, "Sets (Unique Items & Set Operations)")
    unique_numbers: set[int] = {1, 2, 3, 4}
    empty_set: set[int] = set()
    print(f"Initial set: {unique_numbers} | Empty set: {empty_set}")

    unique_numbers.add(5)
    unique_numbers.add(4)  # Duplicate ignored
    unique_numbers.remove(2)
    print(f"After add(5), add(4), and remove(2): {unique_numbers}")

    set_one: set[int] = {1, 2, 3}
    set_two: set[int] = {3, 4, 5}
    print(f"Set 1: {set_one} | Set 2: {set_two}")
    print(f"Union (set_one | set_two): {set_one | set_two}")
    print(f"Intersection (set_one & set_two): {set_one & set_two}")
    print(f"Difference (set_one - set_two): {set_one - set_two}")

    # 5. Exercise 1: Manipulate Data in a Dictionary
    print_sub_section(5, "Exercise 1: Manipulating Data in a Dictionary")
    person: dict[str, str | int] = {
        "name": "Alice",
        "age": 25,
        "grade": "A"
    }
    print(f"Before updates: {person}")

    person["address"] = "123 Main Street"
    person["age"] = 32
    if "grade" in person:
        del person["grade"]

    print(f"After updates: {person}")

    # 6. Exercise 2: Word Frequency Counter
    print_sub_section(6, "Exercise 2: Word Frequency Counter")
    sample_sentence: str = "The AI engineer is the engineer of the future who builds AI tools"
    frequencies: dict[str, int] = count_word_frequency(sample_sentence)
    print(f"Sentence: '{sample_sentence}'")
    print(f"Word frequencies: {frequencies}")

    # 7. Practice 1: Reverse List & Remove Duplicates
    print_sub_section(7, "Practice 1: Reverse List & Remove Duplicates")
    raw_list: list[int] = [10, 20, 20, 30, 40, 40, 50]
    cleaned_list: list[int] = reverse_and_deduplicate(raw_list)
    print(f"Original list: {raw_list}")
    print(f"Reversed & deduplicated: {cleaned_list}")

    # 8. Practice 2: Student Average Grade Calculator
    print_sub_section(8, "Practice 2: Student Average Grade Calculator")
    student_grades: dict[str, float] = {
        "Alice": 92.5,
        "Bob": 85.0,
        "Charlie": 78.5,
        "Diana": 96.0
    }
    avg_grade: float = calculate_average_grade(student_grades)
    print(f"Student grades: {student_grades}")
    print(f"Average grade: {avg_grade:.2f}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
