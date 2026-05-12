
from utils.logger import *

# --- CHAPTER 1: THE FRONT MATTER (Table of Contents) ---
print_header("Table of Contents")
print_toc_entry(1, "Environment Setup")
print_toc_entry(2, "Control Flow Basics")
print_toc_entry(3, "Advanced Logic")

# --- CHAPTER 2: THE CONTENT ---

# Page 1
print_header("Environment Setup")
print_sub_section("Installing Python")
print("Step 1: Download from python.org...")

# Page 2
print_header("Control Flow Basics")

print_sub_section("While Loops")
count = 0
while count < 2:
    print(f"Running iteration {count}")
    count += 1

print_sub_section("For Loops")
for i in range(2):
    print(f"Index: {i}")

# Page 3
print_header("Advanced Logic")
print_sub_section("Nested If-Statements")
print("Logic goes here...")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
