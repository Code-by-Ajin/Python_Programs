"""
Project Title: Fibonacci Series Generator

Description:
Generates the Fibonacci series up to a specified number of terms.
"""

def generate_fibonacci(n):
    """
    Generate Fibonacci series with n terms.

    Args:
        n (int): Number of terms

    Returns:
        list: Fibonacci sequence
    """
    fibonacci_series = []

    a, b = 0, 1

    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b

    return fibonacci_series


def main():
    print("=" * 50)
    print("      FIBONACCI SERIES GENERATOR")
    print("=" * 50)

    try:
        terms = int(input("Enter the number of terms: "))

        if terms <= 0:
            print("Error: Please enter a positive integer.")
            return

        series = generate_fibonacci(terms)

        print("\nFibonacci Series:")
        print(" -> ".join(map(str, series)))

    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

    print("=" * 50)


if __name__ == "__main__":
    main()
