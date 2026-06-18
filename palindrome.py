def is_palindrome(text):
    """
    Check whether the given text is a palindrome.
    Ignores spaces and case differences.
    """
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]


def check_string_palindrome():
    text = input("Enter a string: ")

    if is_palindrome(text):
        print(f'"{text}" is a Palindrome.')
    else:
        print(f'"{text}" is Not a Palindrome.')


def check_number_palindrome():
    number = input("Enter a number: ")

    if not number.isdigit():
        print("Invalid input! Please enter only digits.")
        return

    if is_palindrome(number):
        print(f"{number} is a Palindrome.")
    else:
        print(f"{number} is Not a Palindrome.")


def main():
    while True:
        print("\n===== PALINDROME CHECKER =====")
        print("1. Check String")
        print("2. Check Number")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            check_string_palindrome()

        elif choice == "2":
            check_number_palindrome()

        elif choice == "3":
            print("Thank you for using Palindrome Checker!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
