"""
util.py
Author: Joseph Adogeri
Date: May 12, 2026
Version: 1.0.0
Description: Utility functions for consistent console output formatting 
             during AI Engineering foundational studies.
"""

def print_header(title: str) -> None:
    """
    Prints a prominent, formatted header to the console to mark the start of a main section.
    
    :param title: The text to display inside the header box.
    :return: None
    """
    print("\n" + "="*50)
    print(f" SECTION: {title.upper()}")
    print("="*50)

def print_sub_section(name: str) -> None:
    """
    Prints a formatted sub-section divider to the console for task organization.
    
    :param name: The name of the specific task or sub-section.
    :return: None
    """
    print(f"\n--- Sub-task: {name} ---")

def print_toc_entry(number: int, title: str) -> None:
    """
    Prints a Table of Contents style entry with leading zero padding.
    
    :param number: The entry number (e.g., 1 becomes 01).
    :param title: The description of the entry.
    :return: None
    """
    print(f"{str(number).zfill(2)}. {title}")

if __name__ == "__main__":
    # Quick test to verify the formatting
    print_header("Test Header")
    print_toc_entry(1, "Introduction to AI")
    print_sub_section("Environment Setup")
