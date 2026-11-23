import re
from common.utils import print_header, print_toc_entry, print_sub_section


# --- Sub-section 5: Exercise 1 (Text Cleaner) ---
def clean_text(text: str) -> str:
    # Remove punctuation (keep only word characters and whitespace)
    cleaned: str = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    cleaned = " ".join(cleaned.split())
    # Convert to lowercase
    return cleaned.lower()


# --- Sub-section 6: Exercise 2 (Palindrome Checker) ---
def is_palindrome(text: str) -> bool:
    cleaned: str = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


# --- Sub-section 7: Practice 1 (Count Vowels) ---
def count_vowels(text: str) -> int:
    vowels: str = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


# --- Sub-section 8: Practice 2 (Mask Emails with Regex) ---
def mask_emails(text: str) -> str:
    email_pattern: str = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.sub(email_pattern, "[EMAIL REDACTED]", text)


# --- Sub-section 9: Practice 3 (Reverse Words in a Sentence) ---
def reverse_words(sentence: str) -> str:
    words: list[str] = sentence.split()
    return " ".join(words[::-1])


def main() -> None:
    print_header("Day 5: Working with Strings in Python")
    print_toc_entry(1, "String Manipulation (Concatenation & Slicing)")
    print_toc_entry(2, "String Formatting (f-strings)")
    print_toc_entry(3, "Common String Methods (split, join, replace, strip)")
    print_toc_entry(4, "Regular Expressions (re.search, re.findall, re.sub)")
    print_toc_entry(5, "Exercise 1: Text Cleaner")
    print_toc_entry(6, "Exercise 2: Palindrome Checker")
    print_toc_entry(7, "Practice 1: Count Vowels in a String")
    print_toc_entry(8, "Practice 2: Find & Replace Email Addresses (Regex)")
    print_toc_entry(9, "Practice 3: Reverse Words in a Sentence")

    # 1. String Manipulation (Concatenation & Slicing)
    print_sub_section(1, "String Manipulation (Concatenation & Slicing)")
    first: str = "Hello"
    second: str = "World"
    greeting: str = first + " " + second
    print(f"Concatenated string: {greeting}")

    text: str = "Python Programming"
    print(f"Full text: '{text}'")
    print(f"Slice [0:6]: '{text[0:6]}'")
    print(f"Slice [-11:]: '{text[-11:]}'")

    # 2. String Formatting (f-strings)
    print_sub_section(2, "String Formatting (f-strings)")
    name: str = "Alice"
    age: int = 25
    formatted_message: str = f"My name is {name} and I am {age} years old."
    print(formatted_message)

    # 3. Common String Methods
    print_sub_section(3, "Common String Methods (split, join, replace, strip)")
    sentence: str = "Python is fun"
    words: list[str] = sentence.split()
    print(f"Split by space: {words}")

    csv_sentence: str = "Python,is,fun"
    print(f"Split by comma: {csv_sentence.split(',')}")

    joined_sentence: str = " | ".join(words)
    print(f"Joined with pipe: '{joined_sentence}'")

    language_text: str = "I love Java"
    updated_text: str = language_text.replace("Java", "Python")
    print(f"Replaced text: '{updated_text}'")

    messy_text: str = "    Hello, World!    "
    stripped_text: str = messy_text.strip()
    print(f"Before strip: '{messy_text}' | After strip: '{stripped_text}'")

    # 4. Regular Expressions
    print_sub_section(4, "Regular Expressions (re.search, re.findall, re.sub)")
    contact_info: str = "Contact me at 123-456-7890"
    digits: list[str] = re.findall(r"\d+", contact_info)
    print(f"Original contact: '{contact_info}'")
    print(f"Digits found (re.findall): {digits}")

    masked_contact: str = re.sub(r"\d", "X", contact_info)
    print(f"Masked contact (re.sub): '{masked_contact}'")

    first_match: re.Match[str] | None = re.search(r"\d{3}", contact_info)
    if first_match:
        print(f"First 3-digit match (re.search): '{first_match.group()}'")

    # 5. Exercise 1: Text Cleaner
    print_sub_section(5, "Exercise 1: Text Cleaner")
    raw_input_text: str = "   Hello World!! Welcome to Python, programming...   "
    cleaned_output: str = clean_text(raw_input_text)
    print(f"Raw text: '{raw_input_text}'")
    print(f"Cleaned text: '{cleaned_output}'")

    # 6. Exercise 2: Palindrome Checker
    print_sub_section(6, "Exercise 2: Palindrome Checker")
    test_phrases: list[str] = ["madam", "A man, a plan, a canal, Panama", "Python"]
    for phrase in test_phrases:
        if is_palindrome(phrase):
            print(f"'{phrase}' -> is a palindrome")
        else:
            print(f"'{phrase}' -> is NOT a palindrome")

    # 7. Practice 1: Count Vowels in a String
    print_sub_section(7, "Practice 1: Count Vowels in a String")
    vowel_sample: str = "Foundations of AI Engineering"
    print(f"Text: '{vowel_sample}' | Vowel count: {count_vowels(vowel_sample)}")

    # 8. Practice 2: Find & Replace Email Addresses (Regex)
    print_sub_section(8, "Practice 2: Find & Replace Email Addresses (Regex)")
    email_text: str = "Reach out to alice@example.com or support@company.org for help."
    print(f"Original: '{email_text}'")
    print(f"Redacted: '{mask_emails(email_text)}'")

    # 9. Practice 3: Reverse Words in a Sentence
    print_sub_section(9, "Practice 3: Reverse Words in a Sentence")
    order_sentence: str = "Python is great for AI engineering"
    print(f"Original: '{order_sentence}'")
    print(f"Reversed words: '{reverse_words(order_sentence)}'")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
