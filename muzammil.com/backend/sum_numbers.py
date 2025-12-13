import sys

def calculate_sum():
    """
    Accepts two numbers from the command line using sys.argv and prints their sum.
    Handles potential errors for incorrect number of arguments or non-integer input.
    """
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <number1> <number2>")
        sys.exit(1)

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        total_sum = num1 + num2
        print(f"The sum of {num1} and {num2} is: {total_sum}")
    except ValueError:
        print("Error: Both arguments must be valid integers.")
        sys.exit(1)

if __name__ == "__main__":
    calculate_sum() 