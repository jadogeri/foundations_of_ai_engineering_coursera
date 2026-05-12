from common.utils import print_header, print_toc_entry, print_sub_section

def main(): 
    print_header("Day 1: Introduction to Python Programming")
    print_toc_entry(1, "Data Types and Variables")
    print_sub_section(1, "Data Types and Variables")
    
    #Integers
    my_int: int = 42
    #Floats
    my_float: float = 3.14
    #Strings
    my_string: str = "Hello, AI Engineering!"
    #Booleans
    my_bool: bool = True
    #Lists
    my_list: list[int] = [1, 2, 3, 4, 5]
    #Dictionaries
    my_dict: dict = {"name": "Alice", "age": 30, "is_student": False}
    #Tuples
    my_tuple: tuple[int, int, int] = (10, 20, 30)
    #Sets
    my_set: set[int] = {1, 2, 3, 4, 5}
    #NoneType
    my_none: None = None
    print(f"Integer: {my_int}")
    print(f"Float: {my_float}")
    print(f"String: {my_string}")
    print(f"Boolean: {my_bool}")
    print(f"List: {my_list}")
    print(f"Dictionary: {my_dict}")
    print(f"Tuple: {my_tuple}")
    print(f"Set: {my_set}")
    print(f"NoneType: {my_none}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

