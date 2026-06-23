import math


def check_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"


def check_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def display_result(num):
    print("\n" + "=" * 40)
    print(f"Number Analysis Report")
    print("=" * 40)

    print(f"Input Number : {num}")
    print(f"Sign         : {check_sign(num)}")
    print(f"Type         : {check_even_odd(num)}")

    if check_prime(num):
        print("Prime Status : Prime Number")
    else:
        print("Prime Status : Not a Prime Number")

    print("=" * 40)


def main():
    try:
        number = int(input("Enter an integer: "))
        display_result(number)

    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()
