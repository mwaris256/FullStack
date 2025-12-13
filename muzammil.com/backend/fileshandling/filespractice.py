import json
import os
import csv

#6

file = open('sample.txt', 'r')
content = file.read()
print(content)
file.close()

#7.

file = open('note.txt', 'w')
file.write('''Hey,  
           Whats up!
            How has your day been so far?''')
file.close()

#8. 

with open('diary.txt', 'a') as file:
    file.write('\nDear Diary, today was a good day!')
file = open('diary.txt', 'r')
content = file.readlines()
print(content)

#9.

with open('source.txt','r') as source:
    content = source.read()

with open('destination.txt','w') as destination:
    destination.write(content)

#10.

import re

def count_words_manual(filename):
    """
    Reads a text file and counts word frequency using a dictionary.
    """
    word_counts = {}
    try:
        with open(filename, 'r', encoding='utf8') as file:
            for line in file:
                # Convert to lowercase and find all words
                words = re.findall(r'\b\w+\b', line.lower())
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
        return word_counts
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}

# Example usage:
filename = 'story.txt'
word_frequencies = count_words_manual(filename)
if word_frequencies:
    # Print the results
    for word, count in word_frequencies.items():
        print(f"'{word}': {count}")

#11.

def search_word_in_file(filename, word_to_find):
    """
    Searches for a specific word in a text file and prints the line numbers
    where it is found. Case-insensitive search is performed.
    
    Args:
        filename (str): The name of the file to search.
        word_to_find (str): The word to search for.
    """
    try:
        with open(filename, 'r') as file:
            found_count = 0
            # Iterate through each line in the file, keeping track of the line number (1-based index)
            for line_number, line in enumerate(file, 1):
                # Check if the target word is in the current line (case-insensitive)
                if word_to_find.lower() in line.lower():
                    print(f"Found '{word_to_find}' on line {line_number}: {line.strip()}")
                    found_count += 1

            if found_count == 0:
                print(f"The word '{word_to_find}' was not found in the file.")
            else:
                print(f"\nSearch complete. Found '{word_to_find}' {found_count} time(s).")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"Error reading file: {e}")

# --- Example Usage ---
# 1. Make sure you have a file named 'document.txt' in the same directory.

# Define the file name and the word you want to search for
file_name = 'document.txt'
search_word = 'Japan' # The search is case-insensitive

# Run the function
search_word_in_file(file_name, search_word)

#12.    
with open('poem.txt', 'r') as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.rstrip()) 

#13.

# 1. Define the dictionary you want to save
data_to_write = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science", "History"]
}

file_path = 'data.json'

# --- Writing the dictionary to a JSON file ---
try:
    with open(file_path, 'w') as json_file:
        # Use json.dump() to write the data to the file
        json.dump(data_to_write, json_file, indent=4)
    print(f"Successfully wrote data to '{file_path}'")
except IOError as e:
    print(f"Error writing file: {e}")


# --- Reading the dictionary back from the JSON file ---
data_read_back = None
if os.path.exists(file_path):
    try:
        with open(file_path, 'r') as json_file:
            # Use json.load() to read the data from the file
            data_read_back = json.load(json_file)
        print(f"\nSuccessfully read data back from '{file_path}':")
        print(data_read_back)
        print(f"Type of read data: {type(data_read_back)}")

    except IOError as e:
        print(f"Error reading file: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
else:
    print(f"\nCould not find '{file_path}' to read back.")


# Optional cleanup: remove the file after running the script
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"\nCleaned up and removed '{file_path}'")

#14.

def read_csv_builtin(filename="data.csv"):
    """
    Reads data from a CSV file using Python's built-in csv module 
    and prints each row.
    """
    # Check if file exists in the current working directory
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found in the current directory.")
        print(f"Current working directory: {os.getcwd()}")
        return

    print(f"--- Contents of {filename} (using csv module) ---")
    try:
        # Open the file in read mode ('r')
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            # Create a CSV reader object
            # Use csv.reader for files without a header row
            # Use csv.DictReader if the first row is a header you want to use as keys
            reader = csv.reader(file) 
            # reader = csv.DictReader(file) # Uncomment this line for dict-based reading

            # Iterate over each row in the CSV file
            for row in reader:
                print(row)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# Call the function to run the program
read_csv_builtin()

#15.
    
with open('report.txt', 'r') as file:
    lines = file.readlines()

count = 0
for line in lines:
    count += 1
print(f"There are {count} lines in the file.")
