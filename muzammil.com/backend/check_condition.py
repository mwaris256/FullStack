import sys

def check_condition_and_exit(value):
    """
    Checks if the provided value is negative.
    If it is, the program exits using sys.exit().
    """
    if value < 0:
        print(f"Error: Negative value detected ({value}). Exiting program.")
        sys.exit(1)  # Exit with a non-zero status to indicate an error
    else:
        print(f"Value is non-negative ({value}). Program continues.")

if __name__ == "__main__":
    print("Starting the program...")

    # Test case 1: Value that triggers exit
    print("\n--- Test Case 1: Negative value ---")
    check_condition_and_exit(-5)
    print("This line will not be executed if sys.exit() was called.")

    # Test case 2: Value that allows continuation
    print("\n--- Test Case 2: Non-negative value ---")
    check_condition_and_exit(10)
    print("This line will be executed as the condition was not met.")

    # Test case 3: Another value that allows continuation
    print("\n--- Test Case 3: Zero value ---")
    check_condition_and_exit(0)
    print("This line will also be executed.")

    print("\nProgram finished successfully (if no exit was triggered).")
    sys.exit(0) # Exit with a zero status to indicate successful completion