from common.utils import print_header, print_toc_entry, print_sub_section


def main():
    print_header("Day 2: Control Flow and Logic in Python")
    print_toc_entry(1, "if")
    print_toc_entry(2, "elif")
    print_toc_entry(3, "else")

    # --------------------------------------------------
    # 01. if Statements
    # --------------------------------------------------
    print_sub_section(1, "if Statements")

    temperature: int = 85
    print(f"Current temperature: {temperature}°F")

    if temperature > 80:
        print("It's hot outside! Stay hydrated.")

    # Checking boolean condition
    is_authenticated = True
    if is_authenticated:
        print("Access granted: User is logged in.")

    # --------------------------------------------------
    # 02. elif Statements
    # --------------------------------------------------
    print_sub_section(2, "elif Statements")

    model_accuracy = 0.87
    print(f"Model accuracy: {model_accuracy:.2f}")

    if model_accuracy >= 0.95:
        print("Status: Production ready!")
    elif model_accuracy >= 0.85:
        print("Status: Good performance, minor tuning recommended.")
    elif model_accuracy >= 0.70:
        print("Status: Needs more training data.")

    # --------------------------------------------------
    # 03. else Statements
    # --------------------------------------------------
    print_sub_section(3, "else Statements")

    api_status_code = 500
    print(f"API Response Code: {api_status_code}")

    if api_status_code == 200:
        print("Success: Request completed.")
    elif api_status_code == 404:
        print("Error: Endpoint not found.")
    else:
        print("Fallback: Unexpected server error occurred.")


if __name__ == '__main__':
    main()
