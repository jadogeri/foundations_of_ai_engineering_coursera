from common.utils import print_header, print_toc_entry, print_sub_section

def main(): 
    print_header("Day 2: Control Flow and Logic in Python")
    print_toc_entry(1, "if")
    print_toc_entry(2, "else")
    print_toc_entry(3, "elif")

    print_sub_section(1, "if Statements")
    
    positive_number = 10
    negative_number = -5    
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

