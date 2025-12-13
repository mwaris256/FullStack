def count_vowels(txt):
    count = 0 
    vowels = ['a','e','i','o','u']
    for char in txt.lower():
        if char in vowels:
            count += 1
    return count