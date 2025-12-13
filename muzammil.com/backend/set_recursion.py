import sys

# Get the current recursion limit
original_limit = sys.getrecursionlimit()
print(f"Original recursion limit: {original_limit}")

# Set a new, higher recursion limit
new_limit = 2500  # You can adjust this value as needed
sys.setrecursionlimit(new_limit)

# Get and print the new recursion limit
updated_limit = sys.getrecursionlimit()
print(f"New recursion limit: {updated_limit}")

# Optional: Demonstrate a recursive function that would exceed the original limit
# but works with the new limit.
def deep_recursion(n):
    if n == 0:
        return 0
    else:
        return 1 + deep_recursion(n - 1)

try:
    print(f"Attempting deep recursion up to {new_limit - 50} levels:")
    result = deep_recursion(new_limit - 50)
    print(f"Deep recursion successful, result: {result}")
except RecursionError:
    print("RecursionError: The recursion limit was still exceeded or not set high enough.")