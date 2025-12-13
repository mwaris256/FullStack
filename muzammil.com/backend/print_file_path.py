import sys
import os

# sys.argv[0] contains the name of the script, potentially with a relative path.
script_name_with_path = sys.argv[0]

# To get the absolute path, use os.path.abspath().
absolute_script_path = os.path.abspath(script_name_with_path)

print(f"The file path of the currently running script is: {absolute_script_path}")