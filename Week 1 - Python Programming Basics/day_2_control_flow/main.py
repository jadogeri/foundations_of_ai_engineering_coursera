from common.utils import print_header, print_toc_entry, print_sub_section

def main(): 
    print_header("Day 2: Control Flow and Logic in Python")
    print_toc_entry(1, "if")
    print_toc_entry(2, "else")
    print_toc_entry(3, "elif")
    print_toc_entry(4, "for loop")
    print_toc_entry(5, "while loop")
    print_toc_entry(6, "break and continue")

    print_sub_section(1, "if Statements")
    
    positive_number: int = 10
    negative_number: int = -5
    if positive_number > 0:
        print(f"{positive_number} is a positive number.")
    if negative_number < 0:
        print(f"{negative_number} is a negative number.")
        
    print_sub_section(2, "else Statements")
    if positive_number <= 0:
        print(f"{positive_number} is less than or equal to zero.")
    else:
        print(f"{positive_number} is greater than zero.")

    print_sub_section(3, "elif Statements")
    if positive_number < 0:
        print(f"{positive_number} is a negative number.")
    elif positive_number >= 0:
        print(f"{positive_number} is a positive number.")
    else:
        print(f"{positive_number} is zero.")
        
    print_sub_section(4, "for loop")
    fruits: list[str] = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

    print("looping through list of fruits...")
    for fruit in fruits:
        print(fruit)

    print("\nlooping in range...")

    for loop in range(10):
        print(loop)

    print_sub_section(5, "while loop")
    count: int = 0
    while count < 5:
        print(count)
        count += 1

    print_sub_section(6, "break and continue")
    for number in range(10):
        if number == 5:
            print("Breaking the loop at number 5")
            break
        if number % 2 == 0:
            print(f"Skipping even number: {number}")
            continue
        print(f"printed {number}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

